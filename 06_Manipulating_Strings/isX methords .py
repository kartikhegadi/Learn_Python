"""
isalpha()   : returns TRUE only of letters and isn't blank
isalnum()   : returns TRUE letter consist only of letters and numbers and is not blank
isdecimal() : returns TRUE id the string consist only of numeric character and is not blank
isspace()   : returns TRUE od the string concist only  of space , tabs , and newline and is not blank
istitle()   : returns TRUE if the srting consists only of words that begins with an uppercase letter followed by only lowercase letters
"""

print('kartii'.isalpha())
print('kartiii  '.isalpha())
print('kartii1231'.isalpha())
print('-------------------------')

print('check'.isalnum())
print('check  '.isalnum())
print("check212".isalnum())
print('-------------------------')


print('12123'.isdecimal())
print('131231  '.isdecimal())
print('ajsdj123123'.isdecimal())
print('-------------------------')


print(' '.isspace())
print('ajsda  '.isspace())
print('jajsd\n'.isspace())
print('the names and the strings'.isspace())
print('-------------------------')


print('The Names The Raw String'.istitle())
print('the names the raw string'.istitle())
print('The Names the raw String'.istitle())
print('-------------------------')

