def vote(age):
    if age < 18:
        raise Exception('You cannot Vote')
    else :
        print('You can vote')

try:
    vote(12)
    vote(44)
    vote(33)

except Exception as err:
    print('An exception happned ' + str(err))