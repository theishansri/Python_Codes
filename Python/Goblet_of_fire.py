'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
x=[-1]*100002
school=[]
i=0
for _ in range(int(input())):
    k=list(input().split())
    if(len(k)>1):
        k[1]=int(k[1])
        k[2]=int(k[2])
        if(x[k[1]]==-1):
            x[k[1]]=[k[2]]
            school.append(k[1])
        else:
            x[k[1]].append(k[2])
    else:
        s=school[0]
        print(s,x[s][i])
        if(len(x[s])==1):
            x[s]=-1
            school.remove(s)
            i=0
        else:
            x[s].pop(0)

    
    
        
        
        
    