# First check the version compatibility, then write the HMI display brightness, the GUI unlock code and 
# the nominal frequency of the tri-phased inverters.
# Run this example within the 'examples/' folder using 'python ex_rtu_write_param.py' from a CLI after installing
# nxmodbus package with 'pip install nxmodbus'

import serial
import sys
import os

sys.path.append(os.path.abspath('..'))
from nxmodbus.client_rtu import NextModbusRtu
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
        nextModbus = NextModbusRtu(serial_port, ADDRESS_OFFSET, debug=False)

        # check the version
        if not nextModbus.check_version():
            print("WARNING : The version is not correct")

        value = True  # Earthing scheme disable check at TRUE
        echo = nextModbus.write_parameter(  nextModbus.addresses.device_address_system + INSTANCE,
                                            nextModbus.addresses.system_earthingscheme_disablecheck,
                                            value,
                                            PropType.BOOL)
        assert echo == 1  # a value of 1 is expected on write action, represent the number of registers written
        print('Number of registers written:', echo)

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