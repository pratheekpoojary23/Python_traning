#8 Noen number or Not
num=int(input("enter the number"))
summ=0
temp=num
square=num**2           #square the number

while(square>0):
    digit=square%10      #extract the square digits
    summ=summ+digit       #sum the square digits
    
    square=square//10      # reduce the digit
if temp==summ:
    print("The given number is a Neon number")
else:
    print("the given number is not Neon number")
