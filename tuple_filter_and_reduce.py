# filter

original_tuple=(1,2,3,4,5)
filterd_tuple=tuple(filter(lambda x:x%2==0,original_tuple))
print("original tuple",original_tuple)
print("filtered tuple:",filterd_tuple)

#Reduce

from functools import reduce
def add(x,y):
     return x+y
 
original_tuple=(1,2,3,4,5)
 
result=reduce(add,original_tuple)
print("result of Reducing the Tuple:",result)


