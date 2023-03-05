str=input("Enter the string to convert to lower to upper")

for c in str:
    if c.islower():
        print(c+" is "+c.upper())
    elif c.isupper():
        print(c + " is " + c.lower())

