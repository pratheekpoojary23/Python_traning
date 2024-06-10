lis=[8,9,8,9,8,8,5,5,4,5,4]
K=2
newlis=[]

for i in lis:
    freq=lis.count(i)
    if freq>K:
        newlis.append(i)
print(newlis)