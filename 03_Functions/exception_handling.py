def oyiiy(devideby0):
    try :
        if devideby0 ==1:
            print("😝")
            return 42 / devideby0
    except ZeroDivisionError:
        print("ERROR: INVALID AURGUMENT")

print(oyiiy(2))
print(oyiiy(12))
print(oyiiy(0))
print(oyiiy(1))