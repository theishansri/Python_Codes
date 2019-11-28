# class Node(object):
#     def __init__(self, data):
#         self.data=data
#         self.next=None
#         self.prev=None
#         # self.right=None
# class LinkList(object):
#     def __init__(self):
#         self.head=None
#     def append(self,data):
#         newnode=Node(data)
#         if(self.head is None):
#             self.head=newnode
#         else:
#             curr=self.head
#             while(curr.next):
#                 curr=curr.next
#             curr.next=newnode
#             newnode.prev=curr
#             # newnode.next=None
#     def print(self):
#         temp=self.head
#         while(temp.next!=None):
#             print(temp.data,end=" ")
#             temp=temp.next
#         print(temp.data)
#     def delete(self,s):
#         temp=self.head
#         flag=False
#         m=0
#         while(temp.next and m<s):
#             if(temp.data<temp.next.data):
#                 if(temp.prev is not None):
#                     c=temp.prev
#                     c.next=temp.next
#                     temp.next.prev=c
#                     temp=c
                    
#                 else:
#                     c=temp.next
#                     c.prev=None
#                     temp=c
#                     self.head=c
#                 m+=1
#                 flag=True
#             else:
#                 temp=temp.next
#         if(not flag):
#             c=temp.prev
#             c.next=None
# l12=LinkList()
# for i in range(int(input())):
#     k=list(map(int,input().split()))
#     l=list(map(int,input().split()))
#     m=0
#     if(k[1]>0):
#         for i in l:
#             l12.append(i)
#         l12.delete(k[1])
#     else:
#         print(*l)
# l12.print()
for i in range(int(input())):
    k=list(map(int,input().split()))
    l=list(map(int,input().split()))
    # l12=LinkList()
    m=0
    aux=[]
    if(k[1]>0):
        flag=False
        for i in l:
            if(len(aux)==0 and m<k[1]):
                aux.append(i)
            elif(len(aux)>0):
                if(i<=aux[-1]):
                    aux.append(i)
                else:
                    # c=aux[-1]
                    while(m<k[1] and len(aux)>0 and aux[-1]<i):
                        aux.pop()
                        flag=True
                        m+=1
                    aux.append(i)
        if(not flag):
            aux=l
            aux.pop(-1)
        print(*aux)
    else:
        print(*l)