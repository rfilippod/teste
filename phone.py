from lxml import etree

# Parse the xhstt file
tree = etree.parse('BrazilInstance1.xml')

idResourceType = []

for xml in tree.xpath('//Event'):
    idResourceType.append(xml.attrib.get('Id'))
    idResourceType.append(xml.attrib.get('Name'))

print(idResourceType)

# Extract the root element of the tree
root = tree.getroot()

# Access the elements and attributes of the root element and its children using XPath expressions
for element in root.xpath('//Event'):
    event_id = element.get('ID')
    start_time = element.find('StartDate').text
    end_time = element.find('EndDate').text
    print(event_id, start_time, end_time)
