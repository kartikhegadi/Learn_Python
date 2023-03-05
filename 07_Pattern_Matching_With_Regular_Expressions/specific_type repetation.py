import re
barre=re.compile(r'(ha){12,14}')
mov=barre.search('The advinture of hahahahahahahahahahahahahahaha')
print(mov.group(0))