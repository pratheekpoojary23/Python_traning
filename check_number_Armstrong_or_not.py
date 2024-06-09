#6  ArmStrong number or Not
num=int(input("enter the number"))
summ=0
temp=num
order=len(str(num))

while(num>0):
    r=num%10               #extract each digit
    digit=r**order          #perform power of order
    summ=summ+digit         #find sum
    num=num//10            #reduce the digit
if temp==summ:
    print("The given number is a ArmStrong number")
else:
    print("the given number is not ArmStrong number")