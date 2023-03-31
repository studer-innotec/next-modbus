#!/usr/bin/env python
# -*- coding: utf-8 -*-

from struct import pack, unpack
from pyModbusTCP.client import ModbusClient
from nxmodbus.addresses import Addresses
from nxmodbus.proptypes import PropType
import logging

logger = logging.getLogger(__name__)


class NextModbusTcp:
    """
    This class act as a *Modbus* TCP client in order to communicate with the *Next* gateway (slave)

    Attributes
    ----------
    client: ModbusClient
        Modbus TCP client used for the communication with the gateway.
    addresses: nxmodbus.addresses.Addresses
        Instance of Addresses class grouping all device base addresses and all property modbus addresses
    """

    def __init__(self, server_host, server_port=502, offset=0, debug=False):
        """
        serial device must be configured with the configuration set with the Nx-Interface.\n
        Moreover, a timeout of 1 second must be set.\n
        Parameters
        ----------
        server_host
            Hostname of the TCP server
        server_port
            Port number of the TCP server (default modbus TCP port set as 502)
        offset
            The address offset as defined in the Next device
        debug: boolean
            Activate debug traces for tx/rx frames
        """
        if debug is True:
            logging.basicConfig(level=logging.DEBUG)
        self.addresses = Addresses(offset)
        # Init modbus TCP client
        try:
            self.client = ModbusClient(host=server_host, port=server_port, debug=debug)
        except ValueError as e:
            logger.error("--> Modbus TCP client error : ", str(e))
            return
        self.client.open()

    def __del__(self):
        """
        Explicit destructor
        Ensure to close TCP client
        Returns
        -------
        None
        """
        self.client.close()

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
            # Run this example within the 'examples/' folder using 'python ex_tcp_read_param.py' from a CLI after installing
            # nxmodbus package with 'pip install nxmodbus'

            import sys
            import os

            sys.path.append(os.path.abspath('..'))
            from nxmodbus.client_tcp import NextModbusTcp
            from nxmodbus.proptypes import PropType

            ADDRESS_OFFSET = 0                                      # the modbus address offset as set inside the Next system
            INSTANCE = 0                                            # The instance of the requested device
            SERVER_HOST = "192.168.0.100"                           # ipv4 address of nx-interface
            SERVER_PORT = 502                                       # listening port of nx-interface

            if __name__ == "__main__":

                nextModbus = NextModbusTcp(SERVER_HOST, SERVER_PORT, ADDRESS_OFFSET, False)
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
            return None
        if prop_type == PropType.SIGNAL:
            logger.error("--> PropType.SIGNAL is not readable")
            return None
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
        self.client.unit_id(slave_id)
        if not self.client.is_open():
            if not self.client.open():
                logger.error("--> TCP connection error")
                return None
        try:
            response = self.client.read_holding_registers(reg_addr=address, reg_nb=size)
        except (ValueError, KeyError) as e:
            logger.error("--> Modbus error : " + str(e))
            return None
        else:
            if response is None:
                logger.error("--> Modbus error : " + str(self.client.last_except_txt()))
                return None
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
                return None
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
                logger.error("--> Data type not supported")
                return None

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
        bool
            True if write successful else None

        Example
        --------
        .. code-block:: python

            # First check the version compatibility, then write the HMI display brightness, the GUI unlock code and
            # the nominal frequency of the tri-phased inverters.
            # Run this example within the 'examples/' folder using 'python ex_tcp_write_param.py' from a CLI after installing
            # nxmodbus package with 'pip install nxmodbus'

            import sys
            import os

            sys.path.append(os.path.abspath('..'))
            from nxmodbus.client_tcp import NextModbusTcp
            from nxmodbus.proptypes import PropType

            ADDRESS_OFFSET = 0                                      # the modbus address offset as set inside the Next system
            INSTANCE = 0                                            # The instance of the requested device
            SERVER_HOST = "192.168.0.100"                           # ipv4 address of nx-interface
            SERVER_PORT = 502                                       # listening port of nx-interface

            if __name__ == "__main__":

                nextModbus = NextModbusTcp(SERVER_HOST, SERVER_PORT, ADDRESS_OFFSET, debug=False)

                value = True  # Earthing scheme disable check at TRUE
                ok = nextModbus.write_parameter(nextModbus.addresses.device_address_system + INSTANCE,
                                                nextModbus.addresses.system_earthingscheme_disablecheck,
                                                value,
                                                PropType.BOOL)
                if ok:
                    print('Disable check written successfully')
                else:
                    print('Error when writing disable check')

                value = 10  # Brightness level at 10
                ok = nextModbus.write_parameter(nextModbus.addresses.device_address_nextgateway + INSTANCE,
                                                nextModbus.addresses.nextgateway_hmidisplay_brightness,
                                                value,
                                                PropType.UINT)
                if ok:
                    print('Brightness written successfully')
                else:
                    print('Error when writing brightness')

                value = "12345"  # Unlock code
                ok = nextModbus.write_parameter( nextModbus.addresses.device_address_nextgateway + INSTANCE,
                                                nextModbus.addresses.nextgateway_hmidisplay_unlockcode,
                                                value,
                                                PropType.STRING)
                if ok:
                    print('Unlock code written successfully')
                else:
                    print('Error when writing unlock code')

                value = 50.2  # Nominal frequency of the tri-phased inverters
                ok = nextModbus.write_parameter(nextModbus.addresses.device_address_system,
                                                nextModbus.addresses.system_triphaseinverter_nominalfrequency,
                                                value,
                                                PropType.FLOAT)
                if ok:
                    print('Nominal frequency written successfully')
                else:
                    print('Error when writing nominal frequency')
        """
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
            ba = bytes(value,'UTF-8')
            if len(value) % 2 == 0:
                size = int(len(value) / 2)
            else:
                size = int(len(value) / 2) + 1
                ba += b'\x00'
        else:
            logger.error("--> Data type not supported")
            return None

        unpack_format = '>' + size * 'H'
        registers = unpack(unpack_format, ba)

        self.client.unit_id(slave_id)
        if not self.client.is_open():
            if not self.client.open():
                logger.error("--> TCP connection error")
                return None
        try:
            response = self.client.write_multiple_registers(regs_addr=address, regs_value=registers)
        except (ValueError, KeyError) as e:
            logger.error("--> Modbus error : ", e)
            return None
        else:
            if response is None:
                logger.error("--> Modbus error : " + str(self.client.last_except_txt()))
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
            True if the addresses class version is same as the nx-gateway (minor and major).

        See also
        --------
        None
        """
        omv_remote = self.read_parameter(self.addresses.device_address_nextgateway,
                                            self.addresses.nextgateway_idcard_objectmodelversion,
                                            PropType.UINT)
        if omv_remote is not None:
            ba = pack('>I', omv_remote)
            unpack('>HH', ba)
            omv_major = ba[0] << 8 | ba[1]
            omv_minor = ba[2] << 8 | ba[3]
            logger.debug("--> Gateway OMV version : %s.%s", omv_major, omv_minor)
            logger.debug("--> Class OMV version : %s.%s", self.addresses.version_major, self.addresses.version_minor)
            return omv_major == self.addresses.version_major and \
                    omv_minor == self.addresses.version_minor
