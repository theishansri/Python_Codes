# import heapq
# l=[]
# l1=[]
# i=0
# m={}
# for _ in range(int(input())):
#     s=list(input().split())
#     if(len(s)==1):
#         if(s[0]=='CountHigh'):
#             if(len(l1)>0):
#                 print(m[-l1[0]])
#             else:
#                 print(-1)
#         elif(s[0]=='CountLow'):
#             if(len(l)>0):
#                 print(m[l[0]])
#             else:
#                 print(-1)
#         else:
#             if(len(l)>0 and len(l1)>0):
#                 print(-l1[0]-l[0])
#                 x=l1.pop(0)
#                 y=l.pop(0)
#                 if(m[-x]>0 and m[y]>0):
#                     m[-x]-=1
#                     if(m[y]>0):
#                         m[y]-=1
#                 if(len(l)>0):
#                     l.remove(-x)
#                     l1.remove(-y)
#                 heapq.heapify(l1)
#                 heapq.heapify(l)
#             else:
#                 print(-1)
#     else:
#         s[1]=int(s[1])
#         heapq.heappush(l,s[1])
#         heapq.heappush(l1,-s[1])
#         if(s[1] not in m):
#             m[s[1]]=1
#         else:
#             m[s[1]]+=1
import heapq
l=[]
l1=[]
i=0
m={}
for _ in range(int(input())):
    s=list(input().split())
    if(len(s)==1):
        if(s[0]=='CountHigh'):
            if(len(l)>0):
                print(m[l[-1]])
            else:
                print(-1)
        elif(s[0]=='CountLow'):
            if(len(l)>0):
                print(m[l[0]])
            else:
                print(-1)
        else:
            if(len(l)>0):
                print(l[-1]-l[0])
                x=l.pop(0)
                if(len(l)>0):
                    y=l.pop(-1)
                if(m[x]>0):
                    m[x]-=1
                if(m[y]>0):
                    m[y]-=1
            else:
                print(-1)
    else:
        s[1]=int(s[1])
        if(s[1] not in m):
             m[s[1]]=1
        else:
            m[s[1]]+=1
        l.append(s[1])
        if(len(l)>1 and s[1]>=l[-2]):
            pass
        else:
            l.sort()