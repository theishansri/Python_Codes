class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.height=1
class bst(object):
    def height(self,node):
        if node is None:
            return 0
        else:
            return node.height
    def balance_factor(self,node):
        if(node is None):
            return 0
        return (self.height(node.left)-self.height(node.right))
    def Rotate_Right(self,node):
        b=node.left
        x=b.right
        b.right=node
        node.left=x
        b.height=max(self.height(b.left),self.height(b.right))+1
        node.height=max(self.height(node.left),self.height(node.right))+1
        return b
    def Rotate_Left(self,node):
        b=node.right
        x=b.left
        b.right=node
        node.right=x
        b.height=max(self.height(b.left),self.height(b.right))+1
        node.height=max(self.height(node.left),self.height(node.right))+1
        return b
    def insert(self,root,data):
        if(root is None):
            root=Node(data)
        else:
            if(data<root.data):
                root.left=self.insert(root.left,data)
            elif(data>root.data):
                root.right=self.insert(root.right,data)
        root.height=max(self.height(root.left),self.height(root.right))+1
        bf=self.balance_factor(root)
        if(bf>1 and data<root.data):
            return self.Rotate_Right(root)
        elif(bf<-1 and data>root.data):
            return self.Rotate_Left(root)
        elif(bf>1 and data>root.left.data):
            root.left=self.Rotate_Left(root.left)
            return self.Rotate_Right(root)
        elif(bf<-1 and data<root.right.data):
            root.right=self.Rotate_Right(root.right)
            return self.Rotate_Left(root)
        return root
    def inorder(self,root):
        if(root):
            self.inorder(root.left)
            print(root.data,end='->')
            self.inorder(root.right)

bst=bst()
k1=None
k1=bst.insert(k1,20)
k1=bst.insert(k1,25)
k1=bst.insert(k1,30)
k1=bst.insert(k1,10)
k1=bst.insert(k1,5)
bst.inorder(k1)
print(bst.height(k1))


    
        