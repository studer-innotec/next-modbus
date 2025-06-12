# First check the version compatibility, then write the HMI display brightness,
# set the basic user level code for modbus, and send debug data to Studer Innotec.
# Run this example within the 'examples/' folder using 'python ex_tcp_write_param.py' from a CLI after installing
# nxmodbus package with 'pip install nxmodbus'

import sys
import os

sys.path.append(os.path.abspath('..'))
from nxmodbus.client_tcp import NextModbusTcp

ADDRESS_OFFSET = 0  # the modbus address offset as set inside the Next system
INSTANCE = 0  # The instance of the requested device
SERVER_HOST = "192.168.0.0"  # ipv4 address of nx-interface
SERVER_PORT = 502  # listening port of nx-interface

if __name__ == "__main__":

    nextModbus = NextModbusTcp(SERVER_HOST, SERVER_PORT, ADDRESS_OFFSET, debug=False)

    # check the version
    if not nextModbus.check_version():
        print("WARNING : The version is not correct")

    instance_gateway = 0  # Instance of the gateway. Starts at 0.
    value = 20  # Brightness level at 10
    echo = nextModbus.write_parameter(nextModbus.addresses.device_address_nextgateway + instance_gateway,
                                      nextModbus.addresses.nextgateway_hmidisplay_brightness,
                                      value)

    assert echo == 2  # a value of 2 is expected on write action, represent the number of registers written
    print('Number of registers written:', echo)

    value = "815566"  # Basic user level code for modbus.
    echo = nextModbus.write_parameter(nextModbus.addresses.device_address_nextgateway + instance_gateway,
                                      nextModbus.addresses.nextgateway_modbususerlevel_userlevelcodeinput,
                                      value)
    assert echo == 3  # a value of 3 is expected on write action, represent the number of registers written
    print('Number of registers written:', echo)

    value = 1  # Signal property, we set the value to 1.
    echo = nextModbus.write_parameter(nextModbus.addresses.device_address_nextgateway + instance_gateway,
                                      nextModbus.addresses.nextgateway_webportal_uploaddebugdata,
                                      value)
    # a value of 1 is expected on write action, represent the number of registers written for a bool / signal
    assert echo == 1
    print('Number of registers written:', echo)