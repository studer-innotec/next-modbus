#!/usr/bin/env python
# -*- coding: utf-8 -*-

from struct import pack, unpack
from umodbus.client.serial import rtu
from umodbus.exceptions import *
from nxmodbus.addresses import Addresses
from nxmodbus.proptypes import PropType
import logging

logger = logging.getLogger(__name__)


class NextModbus:
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
        serial device must be configured with the configuration set with the Nx-Interface.\n
        Moreover, a timeout of 1 second must be set.\n
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

    def __del__(self):
        """
        Explicit destructor
        Ensure to close serial device
        Returns
        -------
        None
        """
        self.serial_port.close()

    def read_parameter(self, slave_id, address, prop_type, string_size=0):
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
        prop_type: PropType
            Property type given by the enum found in *proptypes.py*
        string_size: int
            When selecting String as prop_type, it is mandatory to give the string size.

        Returns
        -------
        PropType
            parameter read returned with the given property type.

        Example
        --------
        .. code-block:: python

            # First check the version compatibility, then read the serial number, the modbus tcp port and earthing
            # scheme relay status.
            # Run this example within the 'examples/' folder using 'python ex_read_param.py' from a CLI after installing
            # nxmodbus package with 'pip install nxmodbus'

            import serial
            import sys
            import os

            sys.path.append(os.path.abspath('..'))
            from nxmodbus.client import NextModbus
            from nxmodbus.proptypes import PropType

            SERIAL_PORT_NAME = 'COM4'       # your serial port interface name
            SERIAL_PORT_BAUDRATE = 9600     # baudrate used by your serial interface
            ADDRESS_OFFSET = 0              # your modbus address offset as set inside the Next system
            INSTANCE = 0                    # The instance of the requested device

            if __name__ == "__main__":
                try:
                    serial_port = serial.Serial(SERIAL_PORT_NAME, SERIAL_PORT_BAUDRATE, parity=serial.PARITY_EVEN, timeout=1)
                except serial.serialutil.SerialException as e:
                    print("Check your serial configuration : ", e)
                else:
                    nextModbus = NextModbus(serial_port, ADDRESS_OFFSET, debug=False)

                    # check the version
                    if not nextModbus.check_version():
                        print("WARNING : The version is not correct")

                    # Read the serial number
                    read_value = nextModbus.read_parameter( nextModbus.addresses.device_address_nextgateway + INSTANCE,
                                                            nextModbus.addresses.nextgateway_idcard_serialnumber,
                                                            PropType.STRING,
                                                            8)
                    print('Serial number:', read_value)

                    # Read the modbus TCP port used by the TCP modbus server
                    read_value = nextModbus.read_parameter( nextModbus.addresses.device_address_nextgateway + INSTANCE,
                                                            nextModbus.addresses.nextgateway_modbus_modbustcpport,
                                                            PropType.UINT)
                    print('Modbus TCP port:', read_value)

                    # Read the Earthing relay status
                    read_value = nextModbus.read_parameter( nextModbus.addresses.device_address_system,
                                                            nextModbus.addresses.system_earthingscheme_relayisclosed,
                                                            PropType.BOOL)
                    print('Earthing scheme relay status:', read_value)
        """
        if (prop_type == PropType.STRING or prop_type == PropType.BYTEARRAY) and string_size == 0:
            logger.error("--> string_size parameter mandatory when reading a PropType.STRING")
        if prop_type == PropType.SIGNAL:
            logger.error("--> PropType.SIGNAL is not readable")
        if string_size % 2 == 0:
            size = int(string_size / 2)
        else:
            size = int(string_size / 2) + 1
        if prop_type == PropType.BOOL:
            size = 1
        elif prop_type == PropType.INT or \
                prop_type == PropType.UINT or \
                prop_type == PropType.FLOAT or \
                prop_type == PropType.ENUM or \
                prop_type == PropType.BITFIELD:
            size = 2
        elif prop_type == PropType.INT64 or \
                prop_type == PropType.UINT64 or \
                prop_type == PropType.FLOAT64:
            size = 4
        message = rtu.read_holding_registers(slave_id=slave_id, starting_address=address, quantity=size)
        logger.debug("-> Transmit ADU : 0x%s", str(bytes(message).hex()))
        try:
            response = rtu.send_message(message, self.serial_port)
        except (ValueError, KeyError) as e:
            logger.error(
                "--> Please match your configurations and the values set with the Nx-Interface")
        except IllegalDataAddressError:
            logger.error("--> Illegal Data Address Error : please check the \"Studer Modbus Addresses\" and select a valid address")
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
            elif prop_type == PropType.INT:
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

    def write_parameter(self, slave_id, address, value, prop_type):
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
        prop_type
            Property type

        Returns
        -------
        int
            Quantity of written registers

        Example
        --------
        .. code-block:: python

            # First check the version compatibility, then write the HMI display brightness, the GUI unlock code and 
            # the nominal frequency of the tri-phased inverters.
            # Run this example within the 'examples/' folder using 'python ex_write_param.py' from a CLI after installing
            #   nxmodbus package with 'pip install nxmodbus'

            import serial
            import sys
            import os

            sys.path.append(os.path.abspath('..'))
            from nxmodbus.client import NextModbus
            from nxmodbus.proptypes import PropType

            SERIAL_PORT_NAME = 'COM4'       # your serial port interface name
            SERIAL_PORT_BAUDRATE = 9600     # baudrate used by your serial interface
            ADDRESS_OFFSET = 0              # your modbus address offset as set inside the Next system
            INSTANCE = 0                    # The instance of the requested device

            if __name__ == "__main__":
                try:
                    serial_port = serial.Serial(SERIAL_PORT_NAME, SERIAL_PORT_BAUDRATE, parity=serial.PARITY_EVEN, timeout=1)
                except serial.serialutil.SerialException as e:
                    print("Check your serial configuration : ", e)
                else:
                    nextModbus = NextModbus(serial_port, ADDRESS_OFFSET, debug=False)

                    value = 20  # Brightness level at 10
                    echo = nextModbus.write_parameter(  nextModbus.addresses.device_address_nextgateway + INSTANCE,
                                                        nextModbus.addresses.nextgateway_hmidisplay_brightness,
                                                        value,
                                                        PropType.UINT)

                    assert echo == 2  # a value of 2 is expected on write action, represent the number of registers written
                    print('Number of registers written:', echo)

                    value = "12345"  # Unlock code
                    echo = nextModbus.write_parameter(  nextModbus.addresses.device_address_nextgateway + INSTANCE,
                                                        nextModbus.addresses.nextgateway_hmidisplay_unlockcode,
                                                        value,
                                                        PropType.STRING)
                    assert echo == 3  # a value of 3 is expected on write action, represent the number of registers written
                    print('Number of registers written:', echo)

                    value = 50.2  # Nominal frequency of the tri-phased inverters
                    echo = nextModbus.write_parameter(  nextModbus.addresses.device_address_system,
                                                        nextModbus.addresses.system_triphaseinverter_nominalfrequency,
                                                        value,
                                                        PropType.FLOAT)
                    assert echo == 2  # a value of 3 is expected on write action, represent the number of registers written
                    print('Number of registers written:', echo)
        """
        if prop_type == PropType.BOOL or prop_type == PropType.SIGNAL:
            size = 1
            ba = pack('>?', value)
        elif prop_type == PropType.INT:
            size = 2
            ba = pack('>i', value)
        elif prop_type == PropType.UINT:
            size = 2
            ba = pack('>I', value)
            print(ba)
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
            ba = bytes(value,'UTF-8')
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
                "--> Please match your configurations and the values set with the Nx-Interface")
        except IllegalDataAddressError:
            logger.error("--> Illegal Data Address Error : please check the \"Studer Modbus Addresses\" and select a valid address")
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
        the addresses list.
        A different minor version means that small modifications have been made. Some addresses could be
        removed or added.

        Returns
        -------
        bool
            True if the addresses class version is same as the nx-gateway.

        See also
        --------
        None
        """
        omv_remote = self.read_parameter(self.addresses.device_address_nextgateway, 
                                            self.addresses.nextgateway_idcard_objectmodelversion,
                                            PropType.UINT)
        ba = pack('>I', omv_remote)
        unpack('>HH', ba)
        omv_major = ba[0] << 8 | ba[1]
        omv_minor = ba[2] << 8 | ba[3]
        return omv_major == self.addresses.version_major and \
                omv_minor == self.addresses.version_minor
