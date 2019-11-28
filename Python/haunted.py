import heapq
n,m=map(int,input().split())
l=list(map(int,input().split()))
d={}
p=[]
ma=-9999
ma_age=-999
for i in range(n):
    if(l[i]<=m):
        p.append(-1*l[i])
        if(l[i] not in d):
            d[l[i]]=1
        else:
            d[l[i]]+=1
        if(d[l[i]]>ma):
            ma=d[l[i]]
            ma_age=l[i]
        elif(d[l[i]]==ma and ma_age<l[i]):
            heapq.heapify(p)
            x=-1*heapq.heappop(p)
            ma_age=x
            p.append(-1*x)
        print(ma_age,ma)