while True:
    print('Who are you?')
    name =input()
    if name != 'joe':
        continue
    print('HEllo, Joe. What is the Password?(is ot a fish?)')
    password=input()
    if password == 'swardfish':
        break
print('Access Granted.')