#
lis1=["orange","mango","kiwi","pineapple","banana"]
lis1.sort()
print(lis1)

#
marks=[100,50,65,85,40,48,23]
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)


#Customized sort
# sort based on the how close the number to 50

def fun(n):
    return abs(n-50)

marks=[100,50,65,85,40,48,23]
marks.sort(key=fun)
print(marks)

# case sensitivity
lis2=["orange","mango","Kiwi","Pineapple","banana"]
lis2.sort(key=str.lower)
print(lis2)

# Swap the first and last element of the list

def swap(n):
    a=n[0]
    n[0]=n[-1]
    n[-1]=a
    return n
lis3=[1,2,3,4,5]
print(swap(lis3))

# Swap the given 2  element index of the list

def swaplis(n,pos1,pos2):
    a=n[pos1]
    n[pos1]=n[pos2]
    n[pos2]=a
    return n

lis3=[1,2,3,4,5]
pos1=0
pos2=3
print(swaplis(lis3,pos1-1,pos2-1))

    