n=int(input())
l=list(map(int,input().split()))
x=[l[0]]
l1=[-1]
j=1
i=1
while(i<n):
    next=l[i]
    if(x):
        u=x.pop()
        while(next>u):
            l1.append(next)
            u=x.pop()
        if(u>next):
            l1.append(u) 
    x.append(next)
    i+=1
while(x):
    l1.append(-1)
    x.pop()
print(l1)
                


