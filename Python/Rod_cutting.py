n,m,cap=map(int,input().split())
l=list(map(int,input().split()))
# d={i:0 for i in range(1,m+1)}
d=[0]*(m+1)
c=0
for i in l:
    if(d[i]==cap):
        c+=1
        j=(i%m)+1
        j1=i-1
        while(j!=j1):
            print(j,len(d))
            if(d[j]<cap):
                d[j]+=1
                break
            else:
                j=(j%m)+1
                # print("DSSS",j)
                # if(j>=len(d)):
                #     j=1
    else:
        d[i]+=1
print(c)