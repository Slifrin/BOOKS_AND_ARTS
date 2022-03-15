import xml.etree.ElementTree as xml
from datetime import datetime


# de-serialize
tree = xml.parse('metric.xml')
root = tree.getroot()
print(root.tag)
for child in root:
    print(child.tag)

value = root.find('value') # find child by tag
print('value: ', value.text)

for label in root.findall('./*/label'): # find children by XPATH
    key, value = label.get('key'), label.get('value')
    print(f'key = {key!r}, value = {value!r}')

# serialize

metric = {
    'time' : datetime.now(),
    'name' : 'CPU',
    'value' : 3.4,
    'labels' : {
        'host' : 'prod9',
        'version' : '1.4.4',
    },
}

def new_element(tag, text):
    """Helper function to create an element with text"""
    elem = xml.Element(tag)
    elem.text = text
    return elem

root = xml.Element('metric2')
root.append(new_element('time', metric['time'].isoformat()))
root.append(new_element('name', metric['name']))
root.append(new_element('value', str(metric['value'])))
lables = xml.Element('labels')
for key, value in metric['labels'].items():
    lables.append(xml.Element('label', key=key, value=value))
root.append(lables)
data = xml.tostring(root)
print('New xml', data.decode('utf-8'))
