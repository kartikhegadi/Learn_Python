# while True:
#     print("Enter your name")
#     name=input()
#     if name == 'kartik':
#         break

# while True:
#     print("Who are you")
#     name=input()
#     if name!='kartik':
#         continue
#     print("hello kartik enter your password")
#     pas=input()
#     if pas=='1234':
#         break
# print('Access Granted')

# for i in range(5 , -3, -1):
#     print(i)


# import  copy
# old=[[1,2,3,4],[5,3,2]]
# new=copy.deepcopy(old)
# old[1][0]=11
# print(old)
# print(new)
# old.append(111)
# new.append(33)
# print(old)
# print(new)
#

from pathlib import Path
import os
Path.cwd()
Path.home()
p='/usr/local/bin/python3.9 /usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin/Desktop/python/test_py.py '

print(os.path.dirname(p))

