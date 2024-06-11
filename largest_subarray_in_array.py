
def largest_sun(lis):
    max_sum=cur_sum=lis[0]
    for i in lis[1:]:
        cur_sum=max(i,cur_sum+i)
        max_sum=max(cur_sum,max_sum)
    return max_sum
lst=[-2,1,-3,4,-1,2,1,-5,4]
print(largest_sun(lst))
        