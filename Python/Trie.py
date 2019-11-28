class Node(object):
    def __init__(self,root,data):
        self.data=[data]
        val=True
        next=None
def insert(r,i):
    k=0
    if(r is None):
        Node(r,k)
    else:
        if(i in r):
            insert(r.next,k+1)
        else:
            if(r is None):
                Node(i)
            else:
                r.data.append(Node(i))

x=['abc','fgh','abd']
# r=Node(x[0])
r=None
for i in x:
    insert()

        