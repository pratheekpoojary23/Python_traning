def partition_list(lst,n):
    less_than=[x for x in lst if x<n]
    equal_to=[x for x in lst if x==n]
    greater_than=[x for x in lst if x>n]
    return less_than+equal_to+greater_than

lis=[3,1,4,1,5,9,2,6,5]
pivot=4
print(partition_list(lis,pivot))