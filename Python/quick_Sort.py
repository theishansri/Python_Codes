def partition(a,low,high):
    x=low-1
    key=a[high]
    for j in range(low,high):
        if(a[j]<=key):
            x+=1
            a[x],a[j]=a[j],a[x]
    a[x+1],a[high]=a[high],a[x+1]
    return x+1
def Quick_Sort(a,low,high):
    if(low<high):
        pivot=partition(a,low,high)
        Quick_Sort(a,low,pivot-1)
        Quick_Sort(a,pivot+1,high)
    return a
print(Quick_Sort([5,4,3,2,1],0,4))
