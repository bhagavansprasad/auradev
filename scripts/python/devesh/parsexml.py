import xml.etree.ElementTree as xml
import sys


tree = xml.parse('data.xml')
root = tree.getroot()
print root.tag



# text is empty here
#print root.text

#print "Total students:"
#print root.attrib['recordcount']

#print "Students name"
#for child in root:
#    print child.attrib['name']


print "All rank"
for element in root.iter('rank'):
    print element.text
sys.exit()

print "Devesh rank:"
for element in root.findall('./student[@name="Devesh"]/rank'):
    print element.text

print "First rank student name"
for element in root.findall('./*[rank="1"]'):
    print element.attrib['name']

print "Devesh subject score:"
for element in root.findall('./student[@name="Devesh"]/subject'):
    print element.attrib['name'] + ":" + element.attrib['marks']

print "First rank student subject score:"
for element in root.findall('./student[rank="1"]/subject'):
    print element.attrib['name'] + ":" + element.attrib['marks']
