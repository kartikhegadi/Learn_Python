kar={1:'name',2:'address',3:'no name and no address'}
for val in kar.values():
    print(val)
for key in kar.keys():
    print(key)
for items in kar.items():
    print(items)

#converting key values in the dictionary values in to lists
names=list(kar.keys())
print(names)
names.append('kartii')
print(names)


