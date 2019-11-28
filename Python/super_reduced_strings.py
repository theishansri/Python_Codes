# f=list(input())
# k=[]
# i=0
# while(i<len(f)-1):
#     if(f[i]==f[i+1]):
#         s=f.pop(i)
#         s1=f.pop(i)
#         continue
#     else:
#         i+=1
# print(f)
N,K = input().split()
N=int(N)
K = int(K)
 
A=[int(x) for x in input().split()]
 
if N == 1 and K % 2 == 1:
    print(-1)
    exit()
_max = -1
 
if K <= N:
    _max = max(A[K], _max)
    for i in range(K-1): 
        _max = max(A[i], _max)
    _max = max(A[K], _max)
else:
    _max = max(A)
print(_max)