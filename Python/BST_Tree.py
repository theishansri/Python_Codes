class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def Insert(root,data):
    if(not root):
        root=Node(data)
    else:
        if(data<root.data):
            if(root.left is None):
                root.left=Node(data)
            else:
                Insert(root.left,data)
        elif(data>root.data):
            if(root.right is None):
                root.right=Node(data)
            else:
                Insert(root.right,data)
    return root

def Inorder(root):
    if(root):
        Inorder(root.left)
        print(root.data,end='->')
        Inorder(root.right)
k1=None
k1=Insert(k1,5)
k1=Insert(k1,4)
k1=Insert(k1,3)
k1=Insert(k1,6)
k1=Insert(k1,8)
k1=Insert(k1,9)
Inorder(k1)
