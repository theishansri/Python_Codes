from collections import OrderedDict
n,t=map(int,input().split())
d=OrderedDict()
for i in range(n):
    k=list(input().split())
    k1=int(k[1])
    if k1 in d:
        d[k1].append(k[0])
        d[k1].sort()
    else:
        d[k1]=[k[0]]
s=list(d.keys())
s.sort(reverse=True)
i=0
j=0
print(s,d)
while(i<t):
    if(len(d[s[j]])==1):
        print(d[s[j]][0])
        j+=1
        i+=1
    else:
        m=0
        while(i<t and m<len(d[s[j]])):
            print(d[s[j]][m])
            m+=1
            i+=1