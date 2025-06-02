# This is an example of property reading on an installation with multiple devices.
# TCP protocol is used.
# First check the version compatibility.
# Read the number of next3 devices, and for each device, read the status.
# Read the number of next1 devices, and for each device, read the status.
# Read the number of batteries, and for each battery, read the voltage and the status.
# Read the number of AC source (grid, genset or both), and for each AC source, read the status and the active power
# of each existing phase.
# Run this example within the 'examples/' folder using 'python ex_multi_instances.py' from a CLI after installing
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

    nextModbus = NextModbusTcp(SERVER_HOST, SERVER_PORT, ADDRESS_OFFSET, False)
    # check the version
    if not nextModbus.check_version():
        print("WARNING : The version is not correct")
        sys.exit(-1)

    # Read the number of next3 devices in the installation.
    read_value_nx3_nbr = nextModbus.read_parameter(nextModbus.addresses.device_address_system,
                                                   nextModbus.addresses.system_alldevices_nbrofnext3)
    print('Number of next3:', read_value_nx3_nbr)
    for nx3_instance in range(read_value_nx3_nbr):
        # For each battery, read the status and voltage. Instance starts at 0.
        read_value = nextModbus.read_parameter(nextModbus.addresses.device_address_next3 + nx3_instance,
                                               nextModbus.addresses.next3_next3converter_status)
        print(f"Status of next3 {nx3_instance + 1} : {read_value}")

    # Read the number of next1 devices in the installation.
    read_value_nx1_nbr = nextModbus.read_parameter(nextModbus.addresses.device_address_system,
                                                   nextModbus.addresses.system_alldevices_nbrofnext1)
    print('Number of next1:', read_value_nx1_nbr)
    for nx1_instance in range(read_value_nx1_nbr):
        # For each battery, read the status and voltage. Instance starts at 0.
        read_value = nextModbus.read_parameter(nextModbus.addresses.device_address_next1 + nx1_instance,
                                               nextModbus.addresses.next1_next1_status)
        print(f"Status of next1 {nx1_instance + 1} : {read_value}")

    # Read the number of batteries in the installation.
    read_value_bat_nbr = nextModbus.read_parameter(nextModbus.addresses.device_address_system,
                                                   nextModbus.addresses.system_batterygroupall_nbr)
    print('Number of batteries:', read_value_bat_nbr)
    for bat_instance in range(read_value_bat_nbr):
        # For each battery, read the status and voltage. Instance starts at 0.
        read_value = nextModbus.read_parameter(nextModbus.addresses.device_address_battery + bat_instance,
                                               nextModbus.addresses.battery_battery_status)
        print(f"Status of battery {bat_instance + 1} : {read_value}")
        read_value = nextModbus.read_parameter(nextModbus.addresses.device_address_battery + bat_instance,
                                               nextModbus.addresses.battery_battery_voltage)
        print(f"Voltage of battery {bat_instance + 1} : {read_value}")

    # Read the number of AC source in the installation.
    read_value_ac_source_nbr = nextModbus.read_parameter(nextModbus.addresses.device_address_system,
                                                         nextModbus.addresses.system_systemtotal_acsourcenbr)
    print('Number of AC source:', read_value_ac_source_nbr)
    for ac_source_instance in range(read_value_ac_source_nbr):
        # For each AC source, read the status of the 3 phases and active power. Instance starts at 0.
        # Some phases may not exist in single phase devices. Read phase existance bitfield first.
        # Each phase corresponds to a bit set in the bitfield:
        #   L1 is bit 0 (2^0 = 1)
        #   L2 is bit 1 (2^1 = 2)
        #   L3 is bit 2 (2^2 = 4)
        read_value_phase_existance = nextModbus.read_parameter(
            nextModbus.addresses.device_address_acsource + ac_source_instance,
            nextModbus.addresses.acsource_source_phaseexistance)
        if read_value_phase_existance & 2 ** 0:
            read_value = nextModbus.read_parameter(nextModbus.addresses.device_address_acsource + ac_source_instance,
                                                   nextModbus.addresses.acsource_l1source_status)
            print(f"Status of AC source L1 {ac_source_instance + 1} : {read_value}")
        if read_value_phase_existance & 2 ** 1:
            read_value = nextModbus.read_parameter(nextModbus.addresses.device_address_acsource + ac_source_instance,
                                                   nextModbus.addresses.acsource_l2source_status)
            print(f"Status of AC source L2 {ac_source_instance + 1} : {read_value}")
        if read_value_phase_existance & 2 ** 2:
            read_value = nextModbus.read_parameter(nextModbus.addresses.device_address_acsource + ac_source_instance,
                                                   nextModbus.addresses.acsource_l3source_status)
            print(f"Status of AC source L3 {ac_source_instance + 1} : {read_value}")
        read_value = nextModbus.read_parameter(nextModbus.addresses.device_address_acsource + ac_source_instance,
                                               nextModbus.addresses.acsource_triphasemeasure_totalactivepower)
        print(f"Total active power of AC source {ac_source_instance + 1} : {read_value}")
        print(nextModbus.addresses.next1_idcard_serialnumber,
                                               nextModbus.addresses.next3_idcardconverter_serialnumber)
