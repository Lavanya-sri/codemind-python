t=int(input())
for k in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                temp=a[j+1]
                a[j+1]=a[j]
                a[j]=temp
                c+=1
    if c==0:
        print("0")
    else:
        k=a[n-1]-a[0]
        print(k)