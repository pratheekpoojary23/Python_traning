#O(1)

def access_element(arr,index):
    return arr[index]

liss=[10,20,30,40]
n=2
print(access_element(liss,n))


#O(log n)
#binary searcg

def binary_search(arr,key):
    l=0
    r=len(arr)-1
    
    while(l<=r):
        mid=l+((r-l)//2)
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            r=mid-1
        else:
            l=mid+1
    return -1
ar=[1,2,3,4,5,6,7,8,9]  
k=4
result=binary_search(ar,k)

if result!=-1:
    print("element is found at the index",result)
    
else:
    print("element is not found")
    
    
#binary search recursive approach    
    
def binary_search_recursion(arr,target,left,right):
    if left>right:
        return -1
    mid=(left+right)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]<target:
        return binary_search_recursion(arr,target,mid+1,right)
    else:
        return binary_search_recursion(arr,target,left,mid-1)
    
    
arr=[1,2,3,4,5,6,7,8,9]
target=3
l=0
r=len(arr)-1
result=binary_search_recursion(arr,target,l,r)

if result!=-1:
    print("Element found at index",result) 
else:
    print("Element not found")   
    
    
#O(n)
#linaer search
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr=[1,2,3,4,5,6,7,8,9]
target=4
result=linear_search(arr,target)
if result!=-1:
    print("Element found at index",result)
else:
    print("Element not found")
      
    
#o(N^2)
#bubble sort
def bubble_sort(arr):
    n=len(arr)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    
arr=[60,20,30,40,50,10,80,90,70]
bubble_sort(arr)
print("sorted array:",arr)

#O(2^n)
#fibonacci number using reursion

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=5
result=fibonacci(n)
print("the {}th fibonacci number is {}".format(n,result))



    
