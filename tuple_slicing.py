my_tuple=(1,2,3)
an_tuple=tuple([4,5,6])
print(my_tuple[0])      #accesing first element 
print(my_tuple[-1])   # accesing last element 
print(my_tuple[1:3])  #slicing to get a subset of tuple

combined_tuple=my_tuple+an_tuple
print(combined_tuple)
repeated_tuple=my_tuple*3
print(repeated_tuple)
print(2 in my_tuple)    #output: True
print(4 not in my_tuple)   #output:True
print(len(my_tuple))  #outut:3

for i in my_tuple:
    print(i)
    
string_to_tuple=tuple("hello")
print(string_to_tuple)
list_to_tuple=tuple([1,2,3])
print(list_to_tuple)
print(my_tuple.count(2))    #output:1
print(my_tuple.index(3))    #output:2

