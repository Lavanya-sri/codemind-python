n=int(input())
a=list(map(int,input().split()))
sum=0
for i in range(len(a)):
    sum=0
    temp=a[i]
    while temp!=0:
        r=temp%10
        sum=sum*10+r
        temp=temp//10
    print(sum,end=" ")