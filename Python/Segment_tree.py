import sys
def build_segment_tree(k1,l,start,end,treeNode):
    if(start>end):
        return
    if(start==end):
        k1[treeNode]=l[start]
        return
    mid=(start+end)//2
    build_segment_tree(k1,l,start,mid,2*treeNode)
    build_segment_tree(k1,l,mid+1,end,2*treeNode+1)
    left=k1[2*treeNode]
    right=k1[2*treeNode+1]
    k1[treeNode]=min(left,right)
def query(k1,index,start,end,le,r):
    if(le>end or r<start):
        return sys.maxsize
    if(start>=le and end<=r):
        return k1[index]
    mid=(start+end)//2
    left=query(k1,2*index,start,mid,le,r)
    right=query(k1,(2*index)+1,mid+1,end,le,r)
    return min(left,right)

n,k=map(int,input().split())
l=list(map(int,input().split()))
k1=[-1]*(n*4+1)
build_segment_tree(k1,l,0,n-1,1)
print(k1)
for _ in range(n):
    p,q,r=input().split()
    if(p=='q'):
        print(query(k1,1,0,n-1,int(q),int(r)))
    else:
        l[int(q)]=int(r)
        build_segment_tree(k1,l,0,n-1,1)