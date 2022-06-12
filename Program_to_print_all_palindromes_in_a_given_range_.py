a=int(input())
b=int(input())
for i in range(a,b+1):
    sum=0
    x=i
    while x!=0:
        r=x%10
        sum=(sum*10)+r
        x=x//10
    if sum==i:
        print(i,end=" ")