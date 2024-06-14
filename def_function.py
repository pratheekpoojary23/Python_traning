# default arguments
def myfun(x,y=50):
    print("x :",x)
    print("y :",y)
    
myfun(10)       #in function call the parameter is not passed so directly passed a parameter in function defination


# keyworded argument
def student(firstname,lastname):
    print(firstname,lastname)
    
student(firstname="john",lastname="snow")
student(lastname="snow",firstname="john")


# Non-Keyworded variable length argument(args)
def myfun1(*args):
    print(args)
myfun1("Hello","welcome","to","india")

#using kwargs
def printkwargs(**kwargs):
    print(kwargs)

printkwargs(a="hello",b="world")

#anonymous function
def cube(x):
    return x*x*x

cube_v2=lambda x:x*x*x  
print(cube(7))
print(cube_v2(7))





