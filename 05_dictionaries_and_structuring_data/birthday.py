birthday = {'karthik':'dec 03','69':'nov 5'}

while True:
    print("Enter a name (Blank to quit)")
    name=input()
    if name=='':
        break
    if name in birthday:
        print(birthday[name],'DOB',name)
    else:
        print("i do not have birday info of ",name)
        print('What is bday \n')
        bday=input()
        birthday[name]=bday;
        print("bday is updated in database \n")