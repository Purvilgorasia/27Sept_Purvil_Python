# print factorial  number.

n=int(input("enter a valuue of a ? "))
f=1
if n<0:
    print("error")
else:
    for i in range (1,n+1):
        f=f*i
        print(n,f)

