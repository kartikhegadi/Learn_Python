# enter the starting range number
num1 = int(1)

# enter the ending range number
num2= int(10)

# initialise counter with starting number
cnt = num1

# check until end of the range is achieved
while cnt < num2:

    # if number divisible by 7 and 5
    if cnt % 7 == 0 and cnt % 5 == 0:
        print(cnt, " is divisible by 7 and 5.")

    # increment counter
    cnt += 1