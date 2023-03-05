import re
# heroregx=re.compile(r'Batman | Tina fey')
# mo1=heroregx.search('Batman and tina fey')
# print(mo1.group())

# heroregx=re.compile(r'Bat(man|mobile|coptor|bat)')
# mo1=heroregx.search('Batcoptor and tina fey')
# print(mo1.group())
# print(mo1.group(1))


# optional matching with the question mark
ph_number_regex=re.compile(r'(\d\d\d-)? \d\d\d-\d\d\d\d')
ob=ph_number_regex.search('my phone number is (333)-111-1231')
print(ob.group())

