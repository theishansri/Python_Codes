# from collections import defaultdict
# for _ in range(int(input())):
#     n=int(input())
#     list1=[int(i) for i in input().split()]
#     k1=defaultdict(int)
#     # k1=[]
#     for i in range(n):
#         # print(list1[i])
#         k1[list1[i]]+=1
#     # print(k1)
#     for i in range(n-1):
#         j=i
#         s=0
#         for m in range(j+1,n):
#             if(k1[list1[m]]>k1[list1[i]]):
#                 s+=1
#                 print(list1[m],end=" ")
#                 break
#         if(s==0):
#             print(-1,end=" ")
#     print('\n')
for _ in range(int(input())):
    count={};
    input();
    arr=list(map(int,input().split()));
    for i in arr:
        if i in count:
            count[i]+=1;
        else:
            count[i]=1;
    l=[];
    stack=[];
    for i in range(len(arr)-1,-1,-1):
        while len(stack)>0 and count[stack[-1]]<=count[arr[i]]:
            stack.pop();
        if len(stack)==0:
            l.append(-1);
        else:
            l.append(stack[-1]);
        stack.append(arr[i]);
    print(*l[::-1]);