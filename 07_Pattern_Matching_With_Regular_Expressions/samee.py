import re
barre=re.compile(r'Bat(wo)* ? man')
mov=barre.search('The advinture of Batman')
print(mov.group())
