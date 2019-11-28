t=int(input())
for _ in range(t):
    n,k,p = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    result=p
    for num in a:
        if num <= result:
            result+=1
        if result>n:
            result=-1
            break
    print(result)