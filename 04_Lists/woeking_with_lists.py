catnames=[]
while True:
    print("Enter the names of cats"+str(len(catnames)+1)+'(or enter nothing to stop)')
    name=input()
    if name=='':
        break
    catnames=catnames+[name]

print('The cat names are')
for name in  catnames:
    print(''+name)
