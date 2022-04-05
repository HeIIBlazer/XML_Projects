import xml.etree.ElementTree as ET

'''CURRENCY_PARSE '''
Currency = ET.parse('Currency.xml')
root = Currency.getroot()

roots = []

for item in root.findall('./country'):
    currency = {}
    currency['country'] = item.attrib['name']
    for child in item:
        if child.tag == 'symbol':
            currency['symbol'] = child.text
        if child.tag == 'currency':
            currency['currency'] = child.text
        if child.tag == 'year':
            currency['year'] = child.text

    roots.append(currency)
print(roots)