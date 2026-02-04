#!/usr/bin/env python
# -*- coding: utf-8 -*-

from struct import pack, unpack
from umodbus.client.serial import rtu
from umodbus.exceptions import *
from nxmodbus.addresses import Addresses
from nxmodbus.modbus_object_model import ModbusObjectModel
from nxmodbus.proptypes import PropType
import logging

logger = logging.getLogger(__name__)


class NextModbusRtu:
    """
    This class act as a *Modbus* master in order to communicate with the *Next* gateway (slave)

    Attributes
    ----------
    serial_port: serial.Serial
        Serial port used for communication with the gateway
    addresses: nxmodbus.addresses.Addresses
        Instance of Addresses class grouping all device base addresses and all property modbus addresses
    """

    def __init__(self, serial_port, offset=0, debug=False):
        """
        Serial device must be configured with the configuration set with the next gateway.\n
        Ensure to set a 1-second timeout for all Modbus requests.\n
        Parameters
        ----------
        serial_port
            Instance of serial module
        offset
            The address offset as defined in the Next device
        debug: boolean
            Activate debug traces for tx/rx frames
        """
        self.serial_port = serial_port
        if debug is True:
            logging.basicConfig(level=logging.DEBUG)
        self.addresses = Addresses(offset)
        self.modbus_object_model = ModbusObjectModel(self.addresses)

    def __del__(self):
        """
        Explicit destructor
        Ensure to close serial device
        Returns
        -------
        None
        """
        self.serial_port.close()

    def read_parameter(self, slave_id, address, prop_type=None, string_size=0, read_from_nvm=False):
        """
        Read a parameter from a targeted device according to the given property type.

        Note
        -----
        All parameters listed in the technical specification of the *Next* devices are accessible
        with the *Modbus* protocol.\n

        Parameters
        ----------
        slave_id: int
            Slave identifier number (targeted device)
        address: int
            Register starting address, see "Technical specification - Next Modbus appendix" for
            the complete list of accessible register per device
        prop_type: PropType, optional
            Property type given by the enum found in *proptypes.py*
            This parameter is retained for backward compatibility and is no longer required.
        string_size: int
            When the type of property is a String, it is mandatory to give the string size.
        read_from_nvm: bool
            Read from non-volatile memory. Slow reading operation to be used only when you want to
            retrieve the default user-set value of a property that was previously overwritten by
            a Modbus access

        Returns
        -------
        PropType
            parameter read returned with the given property type.
        """
        if prop_type is None:
            prop_type = self.modbus_object_model.get_prop_type(slave_id, address)
        if prop_type is None:
            logger.error(f"--> Did not find a valid property with slave id {slave_id} and address {address}")
            return None
        if (prop_type == PropType.STRING or prop_type == PropType.BYTEARRAY) and string_size == 0:
            logger.error("--> string_size parameter mandatory when reading a PropType.STRING")
            return None
        if prop_type == PropType.SIGNAL:
            logger.error("--> PropType.SIGNAL is not readable")
            return None
        size = self.modbus_object_model.get_prop_size(slave_id, prop_type, string_size)
        if read_from_nvm:
            message = rtu.read_input_registers(slave_id=slave_id, starting_address=address, quantity=size)
        else:
            message = rtu.read_holding_registers(slave_id=slave_id, starting_address=address, quantity=size)
        logger.debug("-> Transmit ADU : 0x%s", str(bytes(message).hex()))
        try:
            response = rtu.send_message(message, self.serial_port)
        except (ValueError, KeyError) as e:
            logger.error(
                "--> Please match your configurations and the values set with the next gateway")
        except IllegalDataAddressError:
            logger.error(
                "--> Illegal Data Address Error : please check the \"Studer Modbus Addresses\" and select a valid address")
        except IllegalDataValueError:
            logger.error("--> Illegal Data Value Error : please check the PropType or ensure that your system is ready")
        except ModbusError as e:
            logger.error("--> Modbus error : " + str(e))
        else:
            if prop_type == PropType.STRING:
                resp = bytearray()
                for val in response:
                    ba = pack('<H', val)
                    resp = ba + resp
            elif size == 1:
                ba = pack('>B', response[0])
            elif size == 2:
                ba = pack('>HH', response[0], response[1])
            elif size == 4:
                ba = pack('>HHHH', response[0], response[1], response[2], response[3])
            else:
                logger.error("--> Unpossible to unpack the received data")

            if prop_type == PropType.BOOL:
                return unpack('>?', ba)[0]
            elif prop_type == PropType.INT or \
                    prop_type == PropType.ENUM or \
                    prop_type == PropType.BITFIELD:
                return unpack('>i', ba)[0]
            elif prop_type == PropType.UINT:
                return unpack('>I', ba)[0]
            elif prop_type == PropType.INT64:
                return unpack('>q', ba)[0]
            elif prop_type == PropType.UINT64:
                return unpack('>Q', ba)[0]
            elif prop_type == PropType.FLOAT:
                return unpack('>f', ba)[0]
            elif prop_type == PropType.FLOAT64:
                return unpack('>d', ba)[0]
            elif prop_type == PropType.STRING:
                return resp.decode("utf-8")
            else:
                raise Exception("Data type not supported")

    def write_parameter(self, slave_id, address, value, prop_type=None):
        """
         Write a parameter value into a targeted device.

        Note
        -----
        All parameters listed in the technical specification of the *Next* devices are accessible
        with the *Modbus* protocol.

        Parameters
        ----------
        slave_id: int
            Slave identifier number (targeted device)
        address: int
            Register starting address, see "Technical specification - Next Modbus appendix" for
            the complete list of accessible register per device.
        value
            The value to write at the given address.
        prop_type: PropType, optional
            Property type given by the enum found in *proptypes.py*
            This parameter is retained for backward compatibility and is no longer required.

        Returns
        -------
        int
            Quantity of written registers
        """
        if prop_type is None:
            prop_type = self.modbus_object_model.get_prop_type(slave_id, address)
        if prop_type == PropType.BOOL or prop_type == PropType.SIGNAL:
            size = 1
            ba = b'\x00' + pack('>?', value)
        elif prop_type == PropType.INT or \
                prop_type == PropType.ENUM or \
                prop_type == PropType.BITFIELD:
            size = 2
            ba = pack('>i', value)
        elif prop_type == PropType.UINT:
            size = 2
            ba = pack('>I', value)
        elif prop_type == PropType.INT64:
            size = 4
            ba = pack('>q', value)
        elif prop_type == PropType.UINT64:
            size = 4
            ba = pack('>Q', value)
        elif prop_type == PropType.FLOAT:
            size = 2
            ba = pack('>f', value)
        elif prop_type == PropType.FLOAT64:
            size = 4
            ba = pack('>d', value)
        elif prop_type == PropType.STRING:
            ba = bytes(value, 'UTF-8')
            if len(value) % 2 == 0:
                size = int(len(value) / 2)
            else:
                size = int(len(value) / 2) + 1
                ba += b'\x00'
        else:
            raise Exception("Data type not supported")

        unpack_format = '>' + size * 'H'
        registers = unpack(unpack_format, ba)

        message = rtu.write_multiple_registers(slave_id=slave_id, starting_address=address, values=registers)
        logger.debug("-> Transmit ADU : 0x%s", str(bytes(message).hex()))
        try:
            response = rtu.send_message(message, self.serial_port)
        except (ValueError, KeyError) as e:
            logger.error(
                "--> Please match your configurations and the values set with the next gateway")
        except IllegalDataAddressError:
            logger.error(
                "--> Illegal Data Address Error : please check the \"Studer Modbus Addresses\" and select a valid address")
        except IllegalDataValueError:
            logger.error("--> Illegal Data Value Error : please check the PropType or ensure that your system is ready")
        except ModbusError as e:
            logger.error("--> Modbus error : ", e)
        else:
            logger.debug("<- Receive data : 0x%s", str(response))
            return response

    def check_version(self):
        """
        Read the NextGateway parameter which corresponds to the Object Model Version and compare it with
        the version of the generated file *addresses.py*

        Note
        -----
        A different major version means that the compatibility is broken and it is recommanded to update
        the addresses list and modbus type list.
        A different minor version means that small modifications have been made. Some addresses could be
        removed or added.

        Returns
        -------
        bool
            True if the addresses class version and the and modbus object model class is same as the nx-gateway
            (minor and major).
        """
        omv_remote = self.read_parameter(self.addresses.device_address_nextgateway,
                                         self.addresses.nextgateway_idcard_objectmodelversion)
        if omv_remote is not None:
            ba = pack('>I', omv_remote)
            unpack('>HH', ba)
            omv_major = ba[0] << 8 | ba[1]
            omv_minor = ba[2] << 8 | ba[3]
            logger.debug("--> Gateway OMV version : %s.%s", omv_major, omv_minor)
            logger.debug("--> Class OMV version : %s.%s", self.addresses.version_major, self.addresses.version_minor)
            is_major_ok, is_minor_ok = self.modbus_object_model.check_versions(current_omv_major=omv_major,
                                                                               current_omv_minor=omv_minor)
            if not is_major_ok:
                logger.error(
                    '--> Major Object Model Version of the device mismatch with modbus_object_model.py version')
            if not is_minor_ok:
                logger.error(
                    '--> Minor Object Model Version of the device mismatch with modbus_object_model.py version')
            return is_major_ok and is_minor_ok
        return False