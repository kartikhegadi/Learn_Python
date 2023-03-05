import re

phonenumregix=re.compile( r'\d\d\d\-\d\d\d-\d\d\d\d\ ' )
mo=phonenumregix.findall('cell: 123-123-1231 work : 123:432:5311')
print(mo.group())