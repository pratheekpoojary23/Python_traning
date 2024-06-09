#4 Generate a Prime number within the given range
start=int(input("enter the starting number"))
end=int(input("entre the ending number"))
count=0

for num in range(start,end+1):      #forloop for iterate from start to end
    if num>1:                        # 1 is not a prime number
        for i in range(2,num):          
            if(num%i==0):             
                break
        else:
            print(num)
            count=count+1
print("Toatal prime number in a given range=",count)