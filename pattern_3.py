n=int(input("enter the n value"))

for i in range(0,n):
    for j in range(0,n):
        if (i+j>=n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()