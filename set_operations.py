#add 
set={"apple","banana","cherry"}
set.add("orange")
print(set)
print("after add :",set)

#update
set={"apple","banana","cherry"}
tropical={"pineapple","mango","papaya"}
set.update(tropical)
print("after update:",set)

#remove
set={"apple","banana","cherry"}
set.remove("banana")
print("aftre remove:",set)

#discard
set={"apple","banana","cherry"}
set.discard("banana")
print("after discard:",set)

#pop
set={"apple","banana","cherry"}
x=set.pop()
print("poped item:",x)
print("after pop:",set)

#clear
set={"apple","banana","cherry"}
set.clear()
print("after Clear",set)

#del
set={"apple","banana","cherry"}
del set
print(set)

#union(|)
set1={"a","b","c"}
set2={1,2,3}
set3=set1.union(set2)
print("after the union:",set3)

#intersection(&)
set1={"apple","b","c"}
set2={1,"apple",3}
set3=set1.intersection(set2)
print("after the intersection:",set3)

#difference
set1={"a","b","c"}
set2={1,2,3}
set3=set1.difference(set2)
print("after the difference:",set3)

#symmetric difference
set1={"a","b","c"}
set2={1,2,3}
set3=set1.symmetric_difference(set2)
print("after the symmetric difference:",set3)

#intersection_update
set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}
set1.intersection_update(set2)
print("after the intersection_update",set1)

#difference_update
set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}
set1.difference_update(set2)
print("after the difference_update",set1)

#symmetric_difference_update
set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}
set1.symmetric_difference_update(set2)
print("after the symmetric_difference_update",set1)



