# not done yet, still improving ...

import xml.etree.ElementTree as ET
tree = ET.parse('xxxconfig.xml')
root = tree.getroot()
print(root)
i = 0
for child in root:
    i += 1
    print(i, child.tag, child.attrib)

print("\nCustomCrawler below\n")
for CustomCrawler in root.iter('CustomCrawler'):
    print(CustomCrawler.attrib)

print("\nSslCertificate\n")
for SslCertificate in root.iter('SslCertificate'):
    print(SslCertificate.attrib)

'''
print("\ncategoryinstance\n")
for categoryinstance in root.iter('categoryinstance'):
    print(categoryinstance.attrib)
'''

name, bindport, queryport = "Index name", "bindport", "queryport: "
print("%40s %20s %20s" %(name, bindport, queryport))
for Index in root.findall('Index'):
     name = Index.get('name')
     bindport = Index.get('bindport')
     queryport = Index.get('queryport')
     print("%40s %20s %20s" %(name, bindport, queryport))

print("\nabc map crawler info:")
index_abc_map = root[14]
for child in index_abc_map:
    print(child.tag, child.attrib)

print("\nabc map crawler sub level 1 info:")
index_abc_map = root[14][0]
for child in index_abc_map:
    print(child.tag, child.attrib)
