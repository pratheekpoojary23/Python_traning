#7  Happy or UnHappy Number
num=int(input("enter the number"))
res=num
def ishappy(n):   # n is a formal parameter
    summ=0
    while(n>0):
        digit=n%10     # extracting the digit
        summ=summ+digit**2      #squaring the digit and sum the digit
        n=n//10           #reduce the digit
    return summ

while(res!=1 and res!=4):
    res=ishappy(res)       #in this res will be changing until the res=1 or res=4
     
if res==1:
    print("Happy Number")
elif res==4:
    print("unhappy number")
        
