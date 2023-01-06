# function which return reverse of a string

def isPalindrome(s):
    ans =s[::-1]
    print(ans)
    return  s == s[::-1]
# Driver code
s = "1222"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")