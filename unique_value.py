lis=[1,1,2,2,3,4,5,6]
un=[]           #unique list
count=0

for i in lis:
    if i not in un:
        count=count+1
        un.append(i)
print(count)
print(un)