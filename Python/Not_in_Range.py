import sys
def NotinRange (R, L, n):
    # Write your code here
    # l=[]
    s=0
    min_x=sys.maxsize
    max_y=-sys.maxsize
    for i in range(n):
        x=L[i]
        y=R[i]
        if(x<min_x):
            min_x=x
        if(y>max_y):
            max_y=y
        x1=(y-x)+1
        u=x1/2
        u1=u*(x+y)
        s+=u1
    p=(max_y-min_x)+1
    p1=p/2
    p2=p1*(max_y+min_x)
    print(p2-s)
n = 5
L, R = [2,23,21,1001,2002], [20,200,21,2000,999998]
out_ = NotinRange(R, L, n)
print(out_)