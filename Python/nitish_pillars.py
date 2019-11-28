n=int(input())
l=list(map(int,input().split()))
x=[]
for _ in range(int(input())):
    le,r=map(int,input().split())
    x.append(l[le])
    for i in range(1,n):
        x.append(max(x[i-1],l[i]))
    c=0
    for i in range(le,r+1):
        if(l[i]>=x[i]):
            c+=1
    print(c)