# import sys
# def segment_tree(tree,a,index,start,end):
#     if(start>end):
#         return
#     if(start==end):
#         tree[index]=a[start]
#         return
#     mid=(start+end)//2
#     segment_tree(tree,a,2*index,start,mid)
#     segment_tree(tree,a,2*index+1,mid+1,end)
#     left=tree[2*index]
#     right=tree[2*index+1]
#     tree[index]=min(left,right)
# def query(tree,s,e,index,qs,qe):
#     if(qs>e or qe<s):
#         return sys.maxsize
#     if(s>=qs and e<=qe):
#         return tree[index]
#     mid=(s+e)//2
#     left=query(tree,s,mid,2*index,qs,qe)
#     right=query(tree,mid+1,2*index+1,qs,qe)
#     return min(left,right)
# def update(tree,s,e,index,i,value):
#     if(i<s or i>e):
#         return
#     if(s==e):
#         tree[index]=value
#         return 
#     mid=(s+e)//2
#     update(tree,s,mid,2*index,i,value)
#     update(tree,mid+1,e,2*index+1,i,value)
#     tree[index]=min(tree[2*index],tree[2*index+1])
#     return

# n=6
# a=[1,3,2,-2,4,5]
# tree=[None]*(4*n+1)
# index=1
# segment_tree(tree,a,index,0,n-1)
# print(tree)
'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
import sys
def segment_tree(tree,a,index,start,end):
    if(start>end):
        return
    if(start==end):
        tree[index]=a[start]
        return
    mid=(start+end)//2
    segment_tree(tree,a,2*index,start,mid)
    segment_tree(tree,a,2*index+1,mid+1,end)
    left=tree[2*index]
    right=tree[2*index+1]
    tree[index]=min(left,right)
def query(tree,s,e,index,qs,qe):
    if(qs>e or qe<s):
        return sys.maxsize
    if(s>=qs and e<=qe):
        return tree[index]
    mid=(s+e)//2
    left=query(tree,s,mid,2*index,qs,qe)
    right=query(tree,mid+1,e,2*index+1,qs,qe)
    return min(left,right)
def update(tree,s,e,index,i,value):
    if(i<s or i>e):
        return
    if(s==e):
        tree[index]=value
        return 
    mid=(s+e)//2
    update(tree,s,mid,2*index,i,value)
    update(tree,mid+1,e,2*index+1,i,value)
    tree[index]=min(tree[2*index],tree[2*index+1])
    return

n,k=map(int,input().split())
l=list(map(int,input().split()))
tree=[None]*(n*4+1)
segment_tree(tree,l,1,0,n-1)
print(tree)
for _ in range(n):
    p,q,r=input().split()
    q=int(q)
    r=int(r)
    if(p=='q'):
        print(query(tree,0,n-1,1,q,r))
    else:
        update(tree,0,n-1,q,r)
        
        
    
