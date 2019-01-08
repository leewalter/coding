# based on https://github.com/hpreston/python_networking

# Import the jsontodict library
import json

# Open the sample json file and read it into variable
with open("json_example.json") as f:
    json_example = f.read()

# Print the raw json data
print(json_example)

# Parse the json into a Python dictionary
json_dict = json.loads(json_example)

# Save the interface name into a variable
int_name = json_dict["interface"]["name"]

# Print the interface name
print ("\ndumping out interface name: %20s \n" %(int_name))

# Print the whole dict
print("the whole dict is :")
print(json_dict,"\n")

# Change the IP address of the interface
json_dict["interface"]["ipv4"]["address"][0]["ip"] = "192.168.0.123"

# Revert to the json string version of the dictionary
print("the whole json in compact printing is :")
print(json.dumps(json_dict),"\n")

# do pretty printing again
print("the whole json in pretty printing is :")
print(json.dumps(json_dict, sort_keys=True, indent=4))

'''
output:
(base) D:\github\walter-repo\python_networking\data_manipulation\json>python json_dump_and_load1.py
{
    "interface": {
        "name": "GigabitEthernet2",
        "description": "Wide Area Network",
        "enabled": true,
        "ipv4": {
            "address": [
                {
                    "ip": "172.16.0.2",
                    "netmask": "255.255.255.0"
                }
            ]
        }
    }
}


dumping out interface name:     GigabitEthernet2

the whole dict is :
{'interface': {'name': 'GigabitEthernet2', 'description': 'Wide Area Network', 'enabled': True, 'ipv4': {'address': [{'ip': '172.16.0.2', 'netmask': '255.255.255.0'}]}}}

the whole json in compact printing is :
{"interface": {"name": "GigabitEthernet2", "description": "Wide Area Network", "enabled": true, "ipv4": {"address": [{"ip": "192.168.0.123", "netmask": "255.255.255.0"}]}}}

the whole json in pretty printing is :
{
    "interface": {
        "description": "Wide Area Network",
        "enabled": true,
        "ipv4": {
            "address": [
                {
                    "ip": "192.168.0.123",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "name": "GigabitEthernet2"
    }
}

'''
