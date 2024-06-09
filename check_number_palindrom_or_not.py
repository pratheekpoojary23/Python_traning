#11
num=int(input("enter the number"))
org=num
rev=0
while(num>0):
    digit=num%10
    rev=rev*10+digit
    num=num//10

if org==rev:
    print("The given number is a palendrom number")
else:
    print("the given number is not palendrom number")
