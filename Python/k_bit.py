n=int(input())
l=[1]*(n)
for _ in range(int(input())):
    l1,p=map(int,input().split())
    if(l1==1):
        i=0
        index=-1
        c=0
        if(p>n):
            print(-1)
            continue
        while(i<n-1 and c<=p):
            # x=
            # y=l[i+1]
            if(l[i] | l[i+1]):
                c+=1
                index=i if l[i] else i+1
            i+=1
        if(c==p):
            print(index)
        else:
            print(-1)
    else:
        l[p-1]=0