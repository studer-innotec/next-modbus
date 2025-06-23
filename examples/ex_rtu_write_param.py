# First check the version compatibility, then write the HMI display brightness,
# set the basic user level code for modbus, and send debug data to Studer Innotec.
# Run this example within the 'examples/' folder using 'python ex_rtu_write_param.py' from a CLI after installing
# nxmodbus package with 'pip install nxmodbus'

import serial
import sys
import os

sys.path.append(os.path.abspath('..'))
from nxmodbus.client_rtu import NextModbusRtu

SERIAL_PORT_NAME = 'COM4'  # your serial port interface name
SERIAL_PORT_BAUDRATE = 9600  # baudrate used by your serial interface
ADDRESS_OFFSET = 0  # your modbus address offset as set inside the Next system

if __name__ == "__main__":
    try:
        serial_port = serial.Serial(SERIAL_PORT_NAME, SERIAL_PORT_BAUDRATE, parity=serial.PARITY_EVEN, timeout=1)
        nextModbus = NextModbusRtu(serial_port, ADDRESS_OFFSET, debug=False)

        # check the version
        if not nextModbus.check_version():
            raise ValueError("Version check failed")

        instance_gateway = 0  # Instance of the gateway. Starts at 0.
        value = 10  # Brightness level at 10
        echo = nextModbus.write_parameter(nextModbus.addresses.device_address_nextgateway + instance_gateway,
                                          nextModbus.addresses.nextgateway_hmidisplay_brightness,
                                          value)

        assert echo == 2  # a value of 2 is expected on write action, represent the number of registers written
        print('Number of registers written: ', echo)

        value = "815566"  # Basic user level code for modbus.
        echo = nextModbus.write_parameter(nextModbus.addresses.device_address_nextgateway + instance_gateway,
                                          nextModbus.addresses.nextgateway_modbususerlevel_userlevelcodeinput,
                                          value)
        assert echo == 3  # a value of 3 is expected on write action, represent the number of registers written
        print('Number of registers written: ', echo)

        value = 1  # Signal property, we set the value to 1.
        echo = nextModbus.write_parameter(nextModbus.addresses.device_address_nextgateway + instance_gateway,
                                          nextModbus.addresses.nextgateway_webportal_uploaddebugdata,
                                          value)
        # a value of 1 is expected on write action, represent the number of registers written for a bool / signal
        assert echo == 1
        print('Number of registers written: ', echo)
    except serial.serialutil.SerialException as e:
        print('Check your serial configuration : ', e)
    except Exception as e:
        print('Example script returned an error. ', e)



