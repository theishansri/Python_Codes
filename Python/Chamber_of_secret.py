import sys
a,b=map(int,input().split())
m=list(map(int,input().split()))
m1=[m[i] for i in range(b)]

for i in range(b):
    index=-1
    j=-sys.maxsize
    for j1 in range(b):
        if(m1[j1]>j):
            j=m1[j1]
            index=j1
        if(m1[j1]>0):
            m1[j1]-=1
    s=[index+1]
    m1.pop(index)
    m1=s+m1
    print(index+1,end=" ")