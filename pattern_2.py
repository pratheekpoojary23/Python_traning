n=int(input("enter the n number"))

for i in range(0,n):
    for j in range(0,n):
        if (j<=i):
            print("*",end=" ")
    print()
