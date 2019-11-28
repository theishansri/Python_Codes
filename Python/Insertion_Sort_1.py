A=[5,4,3,2,1,0]

for i in range(1,len(A)):
    key=A[i]
    pos=i
    while(i>=0 and A[pos-1]>key):
        A[pos]=A[pos-1]
        pos-=1
    A[pos]=key
print(A)