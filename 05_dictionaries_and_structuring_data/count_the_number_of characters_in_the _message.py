message='Houda, houda yen houdaaa nouda yes yes yes yes'
count= {}

for character in message:
    count.setdefault(character,0)
    count[character]=count[character]+1
print(count)