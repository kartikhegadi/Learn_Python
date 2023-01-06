print('hello'.rjust(23))
print('hello'.ljust(5))
print('hello,world!!'.rjust(20))
print('hello.'.ljust(30))


print('hello'.rjust(20,'#'))
print('hello'.ljust(20,'#'))

print('names'.rjust(20,'$'))

li=['karti','savii','kuntu','prema','arnaya','dhrue']
for i in li:
    print(li.pop().ljust(20,'!'))