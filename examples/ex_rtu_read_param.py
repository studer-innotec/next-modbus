# First check the version compatibility, then read the serial number, the modbus tcp port and earthing
# scheme relay status.
# Run this example within the 'examples/' folder using 'python ex_rtu_read_param.py' from a CLI after installing
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
