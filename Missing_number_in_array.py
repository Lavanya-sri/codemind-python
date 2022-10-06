for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=[]
    for i in range(1,n+1):
        b.append(i)
    for i in a:
        if i in b:
            b.remove(i)
    print(*b)