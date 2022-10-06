n,k,y=map(int,input().split())
a=list(map(int,input().split()))
for i in range(k):
    x=a.pop()
    a.insert(0,x)
for i in range(y):
    z=int(input())
    print(a[z])