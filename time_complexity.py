  # recursion
#def power(n,p):
 #   if p==0:
  #      return 1
   # return(n*power(n,p-1))

#N=5
#P=3
#print(power(N,P))

#using better approach


#if the power is odd then
def power(n,p):
    if p==1:
        return n
    temp=power(n,p/2)
    if(p%2!=0):       #if the power is odd
        return n* temp*temp
    else:
        return temp*temp
    

n=2
p=64
print(power(n,p))