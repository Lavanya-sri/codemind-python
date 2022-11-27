for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    x=0
    for i in range(len(a)):
        if a[i]%2!=0:
            x+=1
    print(x//2)