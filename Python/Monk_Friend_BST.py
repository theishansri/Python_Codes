'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BST(object):
    def __init__(self):
        self.root=None
    def insert(self,root,node):
        # new_node=Node(data)
        if(root is None):
            self.root=node
        else:
            if(node.data<root.data):
                if(root.left is None):
                    root.left=node
                else:
                    self.insert(root.left,node)
            elif(node.data>root.data):
                if(root.right is None):
                    root.right=node
                else:
                    self.insert(root.right,node)
        return self.root
    def search(self,root,data,flag):
        if(root is None):
            print("NO")
            flag=False
        elif(data<root.data):
            return self.search(root.left,data,flag)
        elif(data>root.data):
            return self.search(root.right,data,flag)
        else:
            print("YES")
            flag=True
        return flag
        
    def height(self,root):
        if(root is None):
            return 0
        return max(self.height(root.left),self.height(root.right))+1
for _ in range(int(input())):
    n=list(map(int,input().split()))
    l=list(map(int,input().split()))
    b=BST()
    root=None
    for i in range(n[0]):
        root=b.insert(root,Node(l[i]))
    x=n[1]+n[0]
    for i in range(n[0],x):
        y=b.search(root,l[i],True)
        if(y==False):
            b.insert(root,Node(l[i]))
        