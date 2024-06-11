def peak_ele(lis):
    if not lis:
        return None
    l,r=0,len(lis)-1
    while(l<r):
        mid=l+((r-l)//2)
        if lis[mid]<lis[mid+1]:
            l=mid+1
        else:
            r=mid
    print("the index is",l)         #returning the index
    return lis[l]   # retuning the element
    

listt=[1,2,1,3,5,6,4]
print("the peak element in the list is",peak_ele(listt))