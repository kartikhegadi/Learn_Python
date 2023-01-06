import re
greedyregix=re.compile(r'(ha){3,5}')
mo1=greedyregix.search('Hahahaahahahaa')
print(mo1.group())

nongreedyHaregix=re.compile(r'(ha){3,5}?')
mo2=nongreedyHaregix.search('hahahahaa')
print(mo2.group())