list1=[1,2,3]
list2=["a","b","c"]

#zip the lists into a tuple of pairs
zipped_tuple=tuple(zip(list1,list2))
print("zipped tuple:",zipped_tuple)

#calculating distace between two points
from collections import namedtuple
import math

point=namedtuple("point",["x","y"])

point1=point(1,2)
point2=point(4,6)

distance=math.sqrt((point2.x-point1.x)**2+(point2.y+point1.y)**2)
print("Distance between point1 and point2:",distance)