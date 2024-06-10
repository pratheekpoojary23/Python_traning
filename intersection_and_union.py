lis1=[10,10,20,40]
lis2=[5,10,15]

def list_intersection(lst1,lst2):
    return list(set(lst1) & set(lst2))

print("Intersection:",list_intersection(lis1,lis2))

#


def list_intersection(lst1,lst2):
    return list(set(lst1) | set(lst2))

print("Union:",list_intersection(lis1,lis2))