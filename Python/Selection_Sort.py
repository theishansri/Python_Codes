A=[5,4,3,2,1]
def min_nu(i,A):
    min_a=999999
    for i in range(i,len(A)):
        if(A[i]<min_a):
            min_a=A[i]
            x=i
    return x
for i in range(len(A)):
    x=min_nu(i,A)
    A[i],A[x]=A[x],A[i]
print(A)