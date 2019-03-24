''' 
  this will convert an XML file to a Json file in pretty print ident=4 format
  pip install xmltodict and json first
'''

# Import the xmltodict library
import xmltodict
# Import the dict to json library
import json

# Open the sample xml file and read it into variable
with open("xml_example.xml") as f:
    xml_example = f.read()

# Parse the XML into a Python dictionary
xml_dict = xmltodict.parse(xml_example)

# load the dict into new_json format with pretty print indent = 4

new_json = json.dumps(xml_dict, indent=4)

with open("xml_to_json_example.json","w+") as f:
    json_example = f.write(new_json)
    
'''
sample input : "xml_example.xml"

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

sample output: "xml_to_json_example.json"

{
    "interface": {
        "@xmlns": "ietf-interfaces",
        "name": "GigabitEthernet2",
        "description": "Wide Area Network",
        "enabled": "true",
        "ipv4": {
            "address": {
                "ip": "172.16.0.2",
                "netmask": "255.255.255.0"
            }
        }
    }
}
'''
