# dict={1:'one',2:'two',3:'three',4:'four'}
# print(dict[4])
import pprint

ch={}
messgae='the message what i want to give you is that that is hidden in shell'
for character in messgae:
    print(character,end='\t')
    ch.setdefault(character,0)
    ch[character]=ch[character]+1
pprint.PrettyPrinter(ch)
# pprint.pformat(ch)
# pprint.pprint(ch)
