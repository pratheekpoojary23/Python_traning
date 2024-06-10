l1=[10,20,30,40,50]
print(type(l1))             #list
print(type(l1[0]))          #int

#slicing
print(l1[0:5])
print(l1[::-1])

#Replacing
l2=[" cat","dog","pig","duck"]
print(l2)
l2[3]="cow"
print("After replacing")
print(l2)

#adding

#insert
l2.insert(2,"camel")
print("after insert operation")
print(l2)

#append
l2.append("Elphant")
print("after append operation")
print(l2)

#extend
l3=["Lion","Tiger"]
print("extend operation")
l2.extend(l3)
print(l2)

l3.extend(l2)
print(l3)

#removeing
#pop()
l3.pop(9)
l3.pop(8)
print("after the pop")
print(l3)

#remove()
l3.remove("Elphant")    #removes the first occurence of the "Elephant"
print(l3)

#del
del l3[1]
print(l3)


#checking element in list
#l3=['Lion', ' cat', 'dog', 'camel', 'pig', 'cow']

if "pig" in l3:
    print("exist")
       
#printing using while loop

l3=['Lion', ' cat', 'dog']

i=0
while(i<len(l3)):
    print(l3[i])
    i=i+1
    
#printing using forloop
#iterating over the index

l3=['Lion', ' cat', 'dog']

print("using for loop")
for i in range(0,len(l3)):
    print(l3[i])
   
 
#itering over the values

print("using for loop iterate through values")
for i in l3:
    print(i)