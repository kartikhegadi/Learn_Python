import re
greedyregix=re.compile(r'(ha){7,9}')
mo1=greedyregix.search('Hahahaahahahahahahahahaha')
print(mo1.group())

nongreedyHaregix=re.compile(r'(ha){7,8}?')
mo2=nongreedyHaregix.search('hahahahaahahahahahahahahhahahahaa')

print(mo2.group())