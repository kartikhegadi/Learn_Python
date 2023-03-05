spam={1:'one',2:'two',3:'Three',4:'four'}
for value,items in spam.items():
    print("the value is "+str(value)+"the items is "+str(items))

print('one' in spam.values())

print(list(spam.items()))
