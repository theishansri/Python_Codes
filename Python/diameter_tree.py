'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here\
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
            if(node.data<=root.data):
                if(root.left is None):
                    root.left=node
                else:
                    self.insert(root.left,node)
            else:
                if(root.right is None):
                    root.right=node
                else:
                    self.insert(root.right,node)
        return self.root
    def height(self,root):
        if(root is None):
            return 0
        return max(self.height(root.left),self.height(root.right))+1
n=int(input())
l=list(map(int,input().split()))
b=BST()
root=None
for i in range(n):
    new_node=Node(l[i])
    root=b.insert(root,new_node)
print(b.height(root))
    
