lis=[4,5,6,7,3,8,9]
i,j=3,10
res=True
for ele in lis:
    if ele<i or ele>j:
        res=False
        break
print("Dose List in contains all element inrange: "+str(res))