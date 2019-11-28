A=[5,4,3,2,1,0,-1]

for i in range(len(A)-1):
    for j in range(i+1,len(A)):
        if(A[i]>A[j]):
            A[i],A[j]=A[j],A[i]
print(A)