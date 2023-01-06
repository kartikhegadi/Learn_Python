check={'name':'unnmae','savii':'yesname','noname':'myname'}
print(id(check))

check.setdefault('blackey','hahah')
while True:
    print(id(check))
    name=input("enter the name to search \n")
    print(check)
    print(check.get(name))


