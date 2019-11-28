for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    min_local,local_min,local_max=1,-1,-1
    for i in range(n-1):
        if(min_local==1 and l[i]<l[i+1]):
            # print(i,local_min)
            local_min=i
            min_local=0
        if(l[i]>l[i+1]):
            local_max=i
            print(local_min,local_max)
            min_local=1
            local_min=-1
            local_max=-1
    if(local_min!=-1 and l[-1]>l[local_min]):
        print(local_min,l[-1])