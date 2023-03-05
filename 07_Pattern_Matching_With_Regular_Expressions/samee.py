import re
# #optional
# barre=re.compile(r'Bat(wo) ? man')
# mov=barre.search('The advinture of Batman')
# print(mov.group())

# #zero or more
# barre=re.compile(r'Bat(wo)*  man')
# mov=barre.search('The advinture of Batman')
# print(mov.group())

#one or more
barre=re.compile(r'Bat(wo)*man')
mov=barre.search('The advinture of Batwowowowowowoman')
print(mov.group(0))


