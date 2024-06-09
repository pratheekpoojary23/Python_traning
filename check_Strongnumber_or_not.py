#5 Strong number or Not
num=int(input("enter the number"))
summ=0
temp=num

while(num>0):
    f=1
    i=1
    r=num%10               #extract each digit
    while(i<=r):
        f=f*i              #find factorial
        i=i+1
    summ=summ+f            #find sum
    num=num//10            #reduce the digit
if temp==summ:
    print("The given number is a Strong number")
else:
    print("the given number is not Strong number")