def insertion_sort(a):
    
    for i in range(1,len(a)):
        key=a[i]
        pos=i
        while(pos>0 and key<a[pos-1]):
            a[pos]=a[pos-1]
            pos-=1
        a[pos]=key
    return a
print(insertion_sort([5,4,3,2,1,-1,0]))
