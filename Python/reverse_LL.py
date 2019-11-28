n=int(input())
list1=[int(i) for i in input().split()]
l=[]
m=[]
for i in list1:
    if(i%2==0):
        l.append(i)
    else:
        if(len(l)!=0):
            m+=l[::-1]
            l=[]
        m.append(i)
m+=l[::-1]
print(*m)