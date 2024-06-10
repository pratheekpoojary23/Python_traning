def countocc(n,x):
    count=0
    for i in n:
        if i==x:
            count=count+1
    return count
lis=[10,20,30,40,40,10,40]
x=40
print(countocc(lis,x))