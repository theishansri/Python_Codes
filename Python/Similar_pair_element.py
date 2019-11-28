def SimilarElementsPairs (a,n):
    d={}
    ans=0
    for i in a:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    k=list(d.keys())
    k.sort()
    #print(k)
    i=0
    while i < len(k):
        sum=d[k[i]]
        psum=sum
        while k[i]+1 in d:
            sum+=d[k[i]+1]
            i+=1
        if sum>psum:
            ans+=((sum*(sum-1))//2)
        else:
            i+=1
    return ans

print(SimilarElementsPairs([1,3,5,7,8,2,5,7],8))