import sys
n=int(input())
l=list(map(int,input().split()))
s1=-sys.maxsize
t=0
s=0
for i in l:
    # print(i,li)
    s+=i
    if(s>s1):
        s1=s
        #li.clear()
        t+=1
    if(s<0):
        t=0
        s=0
        
print(t)