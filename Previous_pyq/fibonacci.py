def fibonacci(n):
    if n < 0:
        print("incorrect input")
    elif n == 1:
        return 0
    elif n == 2:  #𝐹0=0,𝐹1=1,𝐹𝑛=𝐹𝑛−1+𝐹𝑛−2,for 𝑛≥2
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)



print("Enter the value of N")
n = int(input())
if n>0:
    x=fibonacci(n)
    print(x)
else:
    print("The value is in valid")
