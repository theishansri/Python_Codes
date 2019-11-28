for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    i=0
    f=0
    while(l):
        if(i==0):
            x=l.pop(0)
            x-=i
            if(x<=0):
                f=1
                break
        else:
            l[0]-=i
            if(l[0]<=0):
                f=1
                break
            else:
                l.pop(0)
        i+=1
            
    if(f):
        print("Goodbye Rick")
    else:
        print("Rick now go and save Carl and Judas")
    print(i)