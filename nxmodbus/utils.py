"""
utils.py
=========

Utility functions for property type extraction and version checking.

Functions
---------

- get_prop_type(slave_id, address, modbus_types: ModbusTypes):: Get the type of a given property from a property id.
- check_version(current_omv_major, current_omv_minor, addresses: Addresses, modbus_types: ModbusTypes): Compare device version with addresses and types files.

"""
from nxmodbus.addresses import Addresses
from nxmodbus.modbus_types import ModbusTypes


def get_prop_type(slave_id, address, modbus_types: ModbusTypes):
    """
        Get the type of a given property from a property id.

        Parameters
        ----------
        slave_id: int
            Slave identifier number (targeted device)
        address: int
            Register starting address, see "Technical specification - Next Modbus appendix" for
            the complete list of accessible register per device
        modbus_types: ModbusTypes
            Instance of ModbusTypes class grouping all device base addresses with types

        Returns
        -------
        prop_type: PropType
            The property type from nxmodbus/proptypes.py or `None` if not found.
        """
    modbus_start_address = slave_id
    all_objects = modbus_types.objects
    for current_object in all_objects:
        if current_object.modbus_device_start_address == modbus_start_address:
            for prop in current_object.props:
                if prop.address == address:
                    prop_type = prop.type
    return prop_type


def check_versions(current_omv_major, current_omv_minor, addresses: Addresses, modbus_types: ModbusTypes):
    """

    Parameters
    ----------
    current_omv_major: int
            Major Object Model Version read from the device.
    current_omv_minor:
            Minor Object Model Version read from the device.
    addresses: Addresses
            Instance of Addresses class grouping all device base addresses and all property modbus addresses
    modbus_types: ModbusTypes
            Instance of ModbusTypes class grouping all device base addresses with types

    Returns
    -------

    """
    return current_omv_major == addresses.version_major and current_omv_minor == addresses.version_minor \
           and current_omv_major == modbus_types.version_major and current_omv_minor == modbus_types.version_minor
