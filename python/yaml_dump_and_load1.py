# based on https://github.com/hpreston/python_networking/tree/master/data_manipulation

# Import the yamltodict library
import yaml

# Open the sample yaml file and read it into variable
with open("yaml_example.yaml") as f:
    yaml_example = f.read()

# Print the raw yaml data
print(yaml_example)

# Parse the yaml into a Python dictionary
yaml_dict = yaml.load(yaml_example)

# Save the interface name into a variable
int_name = yaml_dict["interface"]["name"]

# Print the interface name
print ("\ndumping out interface name: %20s \n" %(int_name))

# Print the whole dict
print("the whole dict is :")
print(yaml_dict,"\n")

# Change the IP address of the interface
yaml_dict["interface"]["ipv4"]["address"][0]["ip"] = "192.168.0.3"

# Change the IP address of the interface
yaml_dict["interface"]["ipv4"]["address"][0]["ip"] = "192.168.0.3"

# Revert to the yaml string version of the dictionary
print("the dump yaml is :\n")
print(yaml.dump(yaml_dict, default_flow_style=False))

'''
input file is 
---
interface:
  name: GigabitEthernet2
  description: Wide Area Network
  enabled: true
  ipv4:
    address:
    - ip: 172.16.0.1
      netmask: 255.255.255.0

output is
(base) D:\github\walter-repo\python_networking\data_manipulation\yaml>python yaml_dump_and_load1.py
---
interface:
  name: GigabitEthernet2
  description: Wide Area Network
  enabled: true
  ipv4:
    address:
    - ip: 172.16.0.1
      netmask: 255.255.255.0

dumping out interface name:     GigabitEthernet2

the whole dict is :
{'interface': {'name': 'GigabitEthernet2', 'description': 'Wide Area Network', 'enabled': True, 'ipv4': {'address': [{'ip': '172.16.0.1', 'netmask': '255.255.255.0'}]}}}

the dump yaml is :

interface:
  description: Wide Area Network
  enabled: true
  ipv4:
    address:
    - ip: 192.168.0.3
      netmask: 255.255.255.0
  name: GigabitEthernet2

  (note name is at the bottom now compared to original input file)

'''
