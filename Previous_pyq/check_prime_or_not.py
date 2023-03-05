def is_prime(n):
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True

n=int(input("enter the number to check the number is prime or not "))
print(is_prime(n))