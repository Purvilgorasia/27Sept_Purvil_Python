a=int(input("Enter integer 1: "))
b=int(input("Enter integer 2: "))

if a==b:
    print("true")
elif a+b==5:
    print("true")
elif a-b==5:
    print("true")
elif b-a==5:
    print("true")
else:
    print("false")