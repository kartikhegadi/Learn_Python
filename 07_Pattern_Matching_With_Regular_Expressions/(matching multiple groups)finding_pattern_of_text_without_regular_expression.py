import re
""" hex=re.compile(r'Batman|Tiny fey')
he=hex.search('batman and Tiny')
print(he.group()) """

bat=re.compile(r'Bat(man|mobile|copter|bat)')
mo=bat.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

#-----------OPETIONAL MATCHING ------------
barre=re.compile(r'Batwom ? man')
mov=barre.search('The advinture of Batwom')
print(mov.group())

