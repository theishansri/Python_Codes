n=int(input())
l=[int(i) for i in input().split()]
mi=l[0]
i=1
print(-1)
while(i<n):
    if(l[i]>mi):
        j=i-1
        while(j>=0):
            if(l[j]<l[i]):
                print(l[j])
                break
            j-=1
    else:
        print(-1)
    if(l[i]<mi):
        mi=l[i]
    i+=1