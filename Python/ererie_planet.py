# import sys
# h,c,q=map(int,input().split())
# k=[]
# mi=sys.maxsize
# ma=-99
# for _ in range(c):
#     hi,si,ei=map(int,input().split())
#     k.append([hi,si,ei])
#     if(mi>si):
#         mi=si
#     if(ma<ei):
#         ma=ei
# print(k)
# for _ in range(q):
#     h,s=map(int,input().split())
#     f=0
#     if(s<mi or s>ma):
#         print("Yes")
#     else:
#         for i in range(c):
#             if(s>=k[i][1] and s<=k[i][2] and h>k[i][0]):
#                 print("Yes")
#                 f=1
#                 break
#         if(f==0):
#             print("No")
def printPairs(arr, arr_size, sum): 
      
    # Create an empty hash set 
    s = set() 
      
    for i in range(0, arr_size): 
        temp = sum-arr[i] 
        if (temp in s): 
            print ("Pair with given sum "+ str(sum) + " is (" + str(arr[i]) + ", " + str(temp) + ")")
        s.add(arr[i]) 
  
# driver program to check the above function 
A = [1, 4, 45, 6, 10, 8] 
n = 16
printPairs(A, len(A), n) 
  