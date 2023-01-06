import re
heroregx=re.compile(r'Batman | Tina fey')
mo1=heroregx.search('Batman and tina fey')
print(mo1.group())
