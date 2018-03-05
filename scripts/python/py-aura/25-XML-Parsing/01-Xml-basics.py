import xml.etree.ElementTree as ET

tree = ET.parse('data.xml')
root = tree.getroot()

print ("root.tag    :", root.tag)
print ("root.attrib :", root.attrib)

print (root.findall("."))
exit(1)

for child in root:
     print (child.tag, child.attrib)

#print (dir(ET))

print (ET.dump(root))
print (ET.Element("COMP_PARTS"))
print ("=" * 10)
print (ET.Element("COMP_PARTS").tag)
print (ET.Element("COMP_PARTS").text)
print (ET.Element("COMP_PARTS").tail)
print (ET.Element("COMP_PARTS").items())
print (ET.Element("COMP_PARTS").keys())
print (ET.Element("COMP_PARTS").getchildren())
print (ET.Element("COMP_PARTS").itertext())
print (dir(ET.Element("COMP_PARTS").itertext()))
exit(1)
print (ET.Element("COMP_PARTS").itertext().next())
exit(1)


