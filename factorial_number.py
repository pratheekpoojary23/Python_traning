#13
num=int(input("enter the number"))

f=1
if num<0:
    print("Factorial does not exists")
elif num==0:
    print("factorial of o is 1")
else:
    for i in range(1,num+1):
        f=f*i
    print("Factorial of the number is",f)
    