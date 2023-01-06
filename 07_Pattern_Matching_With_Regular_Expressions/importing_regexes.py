import re
ph_number_regex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
ob=ph_number_regex.search('my phone number is 333-111-1231')
print('phone number found '+ob.group())

#----------GROUPING WITH PARENTHESEs--------------
ph_number_regex=re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
ob=ph_number_regex.search('my phone number is 333-111-1231')
print(ob.group(0))
print(ob.group(1))
print(ob.group(2))
print(ob.group(3))
#multiple-assignment-trick
#areacode,mainnumber,realno=ob.group()
#print(areacode)
#print(mainnumber)
#print(realno)

#------------STORY OF BACKSHASH------------------
ph_number_regex=re.compile(r'(\(\d\d\d))-(\d\d\d-\d\d\d\d)')
ob=ph_number_regex.search('my phone number is 333-111-1231')
print(ob.group(1))
