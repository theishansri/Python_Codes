class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insert(root,data):
    if(root is None):
        root=Node(data)
    else:
        if(data<=root.data):
            if(root.left is None):
                root.left=Node(data)
            else:
                insert(root.left,data)
        else:
            if(root.right is None):
                root.right=Node(data)
            else:
                insert(root.right,data)
            # root.right=insert(root.right,data)
def delete(r,p,data):
    if(r):
        if(data==r.data):
            if(p.left.data==data):
                p.left=r.left
            elif(p.right.data==data):
                p.right=r.right
        if(data<r.data):
            p=r
            delete(r.left,p,data)
        if(data>r.data):
            p=r
            delete(r.right,p,data)


def inorder(root):
    if(root):
        inorder(root.left)
        print(root.data)
        inorder(root.right)
r=Node(50)
insert(r,20)
insert(r,30)
insert(r,40)
insert(r,10)
insert(r,-10)
insert(r,5)
inorder(r)
delete(r,r,-10)
print("****")
inorder(r)