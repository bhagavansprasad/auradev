import xml.etree.cElementTree as ET

tree = ET.ElementTree(file='1d.xml')

root = tree.getroot()
print(root.tag, root.attrib)

print(root[0].tag, root[0].text)

for elem in root:
    print(elem.tag, elem.attrib)

print("")

for elem in tree.iter(tag='student'):
    print(elem.tag, elem.attrib)

for elem in tree.iterfind('student/family-details'):
    print(elem.tag, elem.attrib)

for elem in tree.iterfind('branch[@name="hema"]'):
    print(elem.tag, elem.attrib)
exit(1)

