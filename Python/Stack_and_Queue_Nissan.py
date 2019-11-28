n,k = map(int, input().split())
a = [int(i) for i in input().split()]
#a.sort(reverse=True)
s=0
for i in range(k):
    s+=a[i]
m=s
for i in range(k-1):
    s=s+a[n-1-i]-a[k-1-i]
    if(s>=m):
        m=s
print(m)