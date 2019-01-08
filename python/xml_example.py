# based on https://github.com/hpreston/python_networking

# Import the xmltodict library
import xmltodict

# Open the sample xml file and read it into variable
with open("xml_example.xml") as f:
    xml_example = f.read()

# Print the raw XML data
print(xml_example)

# Parse the XML into a Python dictionary
xml_dict = xmltodict.parse(xml_example)

# Save the interface name into a variable using XML nodes as keys
int_name = xml_dict["interface"]["name"]

# Print the interface name
print(int_name)

# Change the IP address of the interface
xml_dict["interface"]["ipv4"]["address"]["ip"] = "192.168.0.123"

# Revert to the XML string version of the dictionary
print(xmltodict.unparse(xml_dict))

'''
(base) D:\github\walter-repo\python_networking\data_manipulation\xml>python xml_example.py
<?xml version="1.0" encoding="UTF-8" ?>
<interface xmlns="ietf-interfaces">
  <name>GigabitEthernet2</name>
  <description>Wide Area Network</description>
  <enabled>true</enabled>
  <ipv4>
    <address>
      <ip>172.16.0.2</ip>
      <netmask>255.255.255.0</netmask>
    </address>
  </ipv4>
</interface>

GigabitEthernet2
<?xml version="1.0" encoding="utf-8"?>
<interface xmlns="ietf-interfaces"><name>GigabitEthernet2</name><description>Wide Area Network</description><enabled>true</enabled><ipv4><address><ip>192.168.0.123</ip><netmask>255.255.255.0</netmask></address></ipv4></interface>
'''
