# This is an example of property reading on an installation with multiple devices.
# TCP protocol is used.
# First check the version compatibility.
# Read the number of next3 devices, and for each device, read the connection state of the AUX relay n°1.
# Read the number of next1 devices, and for each device, read the connection state of the AUX relay n°1.
# Read the number of batteries, and for each battery, read the voltage and the state of charge (SoC).
# Read the number of AC input (grid, genset or both), and for each AC input, read the active power
# of each existing phase and the total active power.
# Run this example within the 'examples/' folder using 'python ex_multi_instances.py' from a CLI after installing
# nxmodbus package with 'pip install nxmodbus'

import sys
import os

sys.path.append(os.path.abspath('..'))

from nxmodbus.client_tcp import NextModbusTcp

ADDRESS_OFFSET = 0  # the modbus address offset as set inside the Next system
SERVER_HOST = "192.168.0.1"  # ipv4 address of nx gateway
SERVER_PORT = 502  # listening port of nx-interface

if __name__ == "__main__":
    try:
        nextModbus = NextModbusTcp(SERVER_HOST, SERVER_PORT, ADDRESS_OFFSET, False)
        # check the version
        if not nextModbus.check_version():
            raise ValueError("Version check failed")

        # Read the number of next3 devices in the installation.
        read_value_nx3_nbr = nextModbus.read_parameter(nextModbus.addresses.device_address_system,
                                                       nextModbus.addresses.system_alldevices_nbrofnext3)
        print('Number of next3: ', read_value_nx3_nbr)
        for nx3_instance in range(read_value_nx3_nbr):
            # For each next3 device, read if the the AUX relay is connected. Instance starts at 0.
            read_value = nextModbus.read_parameter(nextModbus.addresses.device_address_next3 + nx3_instance,
                                                   nextModbus.addresses.next3_relayaux1_isconnected)
            print(f"Relay AUX 1 of next3 {nx3_instance + 1} is connected ? {read_value}")

        # Read the number of next1 devices in the installation.
        read_value_nx1_nbr = nextModbus.read_parameter(nextModbus.addresses.device_address_system,
                                                       nextModbus.addresses.system_alldevices_nbrofnext1)
        print('Number of next1: ', read_value_nx1_nbr)
        for nx1_instance in range(read_value_nx1_nbr):
            # For each next1 device, read if the the AUX relay is connected. Instance starts at 0.
            read_value = nextModbus.read_parameter(nextModbus.addresses.device_address_next1 + nx1_instance,
                                                   nextModbus.addresses.next1_relayaux1_isconnected)
            print(f"Relay AUX 1 of next1 {nx1_instance + 1} is connected ? {read_value}")

        # Read the number of batteries in the installation.
        read_value_bat_nbr = nextModbus.read_parameter(nextModbus.addresses.device_address_system,
                                                       nextModbus.addresses.system_batterygroupall_nbr)
        print('Number of batteries: ', read_value_bat_nbr)
        for bat_instance in range(read_value_bat_nbr):
            # For each battery, read the State of Charge (SoC) and voltage. Instance starts at 0.
            read_value = nextModbus.read_parameter(nextModbus.addresses.device_address_battery + bat_instance,
                                                   nextModbus.addresses.battery_batterycommon_socinpercent)
            print(f"State of charge of battery {bat_instance + 1} : {read_value}")
            read_value = nextModbus.read_parameter(nextModbus.addresses.device_address_battery + bat_instance,
                                                   nextModbus.addresses.battery_battery_voltage)
            print(f"Voltage of battery {bat_instance + 1} : {read_value}")

        # Read the number of AC input in the installation.
        read_value_ac_input_nbr = nextModbus.read_parameter(nextModbus.addresses.device_address_system,
                                                            nextModbus.addresses.system_systemtotal_acsourcenbr)
        print('Number of AC input: ', read_value_ac_input_nbr)
        for ac_input_instance in range(read_value_ac_input_nbr):
            # For each AC input, read the active power of the 3 phases and the total active power. Instance starts at 0.
            # Some phases may not exist in single phase devices. Read phase existance bitfield first.
            # Each phase corresponds to a bit set in the bitfield:
            #   L1 is bit 0 (2^0 = 1)
            #   L2 is bit 1 (2^1 = 2)
            #   L3 is bit 2 (2^2 = 4)
            read_value_phase_existance = nextModbus.read_parameter(
                nextModbus.addresses.device_address_acsource + ac_input_instance,
                nextModbus.addresses.acsource_source_phaseexistance)
            if read_value_phase_existance & 2 ** 0:
                read_value = nextModbus.read_parameter(nextModbus.addresses.device_address_acsource + ac_input_instance,
                                                       nextModbus.addresses.acsource_l1measure_activepower)
                print(f"Active power of AC input {ac_input_instance + 1} L1 : {read_value}")
            if read_value_phase_existance & 2 ** 1:
                read_value = nextModbus.read_parameter(nextModbus.addresses.device_address_acsource + ac_input_instance,
                                                       nextModbus.addresses.acsource_l2measure_activepower)
                print(f"Active power of AC input {ac_input_instance + 1} L2 : {read_value}")
            if read_value_phase_existance & 2 ** 2:
                read_value = nextModbus.read_parameter(nextModbus.addresses.device_address_acsource + ac_input_instance,
                                                       nextModbus.addresses.acsource_l3measure_activepower)
                print(f"Active power of AC input {ac_input_instance + 1} L3 : {read_value}")
            read_value = nextModbus.read_parameter(nextModbus.addresses.device_address_acsource + ac_input_instance,
                                                   nextModbus.addresses.acsource_triphasemeasure_totalactivepower)
            print(f"Total active power of AC input {ac_input_instance + 1} : {read_value}")
    except Exception as e:
        print(f"Example script returned an error. {e}")
