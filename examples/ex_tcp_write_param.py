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
    
    # check the version
    if not nextModbus.check_version():
        print("WARNING : The version is not correct")

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