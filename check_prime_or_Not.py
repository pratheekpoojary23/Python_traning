#3 Check for Prime number or not
num=int(input("Enter the number"))

if num<=1:
    print(num,"is not prime number")
elif num>1:
    for i in range(2,num):
        if(num%i==0):
            print("NOT a prime number")
            break
    else:  
        print("Prime number")