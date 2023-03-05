"""Define a Python function with suitable parameters to generate prime numbers between two integer
values. Write a Python program which accepts two integer values m and n (note: m>0, n>0 and m < n)
as inputs and pass these values to the function. Suitable error messages should be displayed if the
conditions for input values are not followed."""

def prime(m, n):
    for num in range(m, n + 1):
        if num > 1: # one is a prime number
            for i in range(2, num):  # becz 2 is prime number
                if (num % i) == 0:
                    break
            else:
                print(num)

print("Enter the range of numbers to find prime numbers")

m = int(input("Enter the value for m"))
n = int(input("Enter the value for n"))
if m>0 and n>0 and m<n:
    prime(m, n)
else:
    print("Enter the correct values")