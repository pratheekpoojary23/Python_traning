#9  Spy number or Not
num=int(input("enter the number"))
summ=0
product=1
while(num>0):
    digit=num%10      #extract the num digits
    summ=summ+digit     #sum of the digit
    product=product*digit  #product of digit
    num=num//10            #reduce the digit
    
if product==summ:
    print("The given number is a Spy number")
else:
    print("the given number is not Spy number")
    
    