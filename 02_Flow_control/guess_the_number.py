import random
secret_number=random.randint(1,20)
print("I am thinking of a number between 1 and 20")

#ask for a number only he/she should guess for 5 times

for guess_time in range(1,7):
    print("Take a guess")
    guess = int(input())

    if guess <secret_number:
        print("Your guess is too  low")
    elif guess > secret_number:
        print("guess is too high")
    else :
        break #condition for right guess

if guess == secret_number :
    print("Good job! you have guessed my number"+str(guess_time)+'Huesses!')
else:
    print("Nope the number i was thinking of was "+str(secret_number))