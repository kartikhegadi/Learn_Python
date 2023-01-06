def printPicnic(itemsdist,leftwidth,rightwidth):
    print('PICNIC ITEMS'.center(leftwidth+rightwidth,'-'))
    for k, v in itemsdist.items():
        print(k.ljust(leftwidth,'-')+str(v).rjust(rightwidth))



picnicitems={ 'sandwiches':4, 'apple':12,'cups':4,'cookies':10}
printPicnic(picnicitems,12,5)
for i,j in picnicitems.items():
    print(i.ljust(20,'-'),j)


