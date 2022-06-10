n,m=map(int,input().split())
a=[list(map(int,input().split()))
for i in range(n)]
for j in range(0,m):
    max=0
    for i in range(0,n):
        if a[i][j]>max:
            max=a[i][j]
    print(max)