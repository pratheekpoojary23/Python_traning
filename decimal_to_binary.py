def btod(d):
    b=''
    if d==0:
        return
    while(d>0):
        b=str(d%2)+b
        d=d//2
    return b

d=22
b=btod(d)
print("binary to decimal convert of",d,"is",b)