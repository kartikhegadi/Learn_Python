import copy

old_ayoo=[1,2,3,4,5]
new_ayoo=copy.copy(old_ayoo)
old_ayoo[0]='namee'

print(id(old_ayoo)," the list is ",old_ayoo)
print(id(new_ayoo),"the list is ",new_ayoo)


