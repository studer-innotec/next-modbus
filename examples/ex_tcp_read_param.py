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

    # Read the Earthing relay status from Flash
    read_value = nextModbus.read_parameter( nextModbus.addresses.device_address_system,
                                            nextModbus.addresses.system_earthingscheme_relayisclosed,
                                            PropType.BOOL,
                                            read_from_flash=True)
    print('Earthing scheme relay status from flash:', read_value)