#sorting  
tuple_of_int=(5,2,8,1,3)
sorted_tuple=tuple(sorted(tuple_of_int))
print("Sorted Tuple:",sorted_tuple)



tuple_of_tuple=((1,"apple"),(3,"orange"),(2,"banana"))
sorted_tuple=sorted(tuple_of_tuple,key=lambda x:x[1])
print("sorted tuple:",sorted_tuple)



#tuple comprehension to create a tupel of square
square_tuple=tuple(x**2 for x in range(1,6))
print("Squares tuple:",square_tuple)