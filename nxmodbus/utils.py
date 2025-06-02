from nxmodbus.addresses import Addresses
from nxmodbus.modbus_types import ModbusTypes
from nxmodbus.proptypes import PropType



def get_type_and_string_length(slave_id, address, modbus_types: ModbusTypes):
    prop_type = None
    string_size = None
    modbus_start_address = slave_id
    all_objects = modbus_types.objects
    for current_object in all_objects:
        if current_object.modbus_device_start_address == modbus_start_address:
            for prop in current_object.props:
                if prop.address == address:
                    prop_type = prop.type
                    if prop_type == PropType.STRING:
                        string_size = prop.string_size
    return prop_type, string_size


def check_versions(current_omv_major, current_omv_minor, addresses: Addresses, modbus_types: ModbusTypes):
    return current_omv_major == addresses.version_major and current_omv_minor == addresses.version_minor \
           and current_omv_major == modbus_types.version_major and current_omv_minor == modbus_types.version_minor

