list1=[]
n=int(input())
for _ in range(n):
    list1.append(int(input()))
list2=[-1]*n
list3=[-1]*n
x=[-1]
y=[list1[-1]]
for i in range(n-1,-1,-1):
    if(list1[i]<x[-1]):
        list3[i]=x[-1]
    else:
        list3[i]=-1
    x.append(max(x[-1],list1[i]))
    if(list1[i]>y[-1]):
        list2[i]=y[-1]
    else:
        list2[i]=-1
    y.append(min(y[-1],list1[i]))
print(list2)
for i in range(n-1,-1,-1):
    if(list1[i]>list3[i]):
        list3[i]=-1
    else:
        if(list3[i]!=-1):
            s=i+1
            while(s<len(list1)):
                if(list1[i]<list1[s]):
                    list3[i]=list1[s]
                    f=1
                    break
                s+=1
    if(list3[i]==-1):
        list2[i]=-1
    else:
        s=i+1
        f=0
        while(s<n):
            if(list3[i]>list1[s]):
                list2[i]=list1[s]
                f=1
                break
            s+=1
        if(not f):
            list2[i]=-1
print(list3)
print(list2)






    