"""# Function to Convert Celsius into Fahrenheit.
def Fahrenheit_Temp(Tc):
    try:
       return ((Tc*1.8)+32)
    except ZeroDivisionError :
        print("The Tc is ZERO")



# Driver.
Celsius = int(input('Enter the Temperature on Celsius scale.'))
print("The temperature on Fahrenheit Scale is:")
print(Fahrenheit_Temp(Celsius))"""



inp = input('Enter celcious Temperature:')
try:
    cel = float(inp)
    far = cel* 9/5+32
    print(cel)
except ZeroDivisionError :
    print('Please enter a number')