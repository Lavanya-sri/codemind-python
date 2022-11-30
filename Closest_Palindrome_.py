n=int(input())
temp=n
le=0
rg=0
for i in range(n-1,0,-1):
    k=i
    sum=0
    while(k>0):
        r=k%10
        sum=sum*10+r
        k=k//10
    if(sum==i):
        le=i
        break
for i in range(n+1,10000,1):
    k=i
    sum=0
    while(k>0):
        r=k%10
        sum=sum*10+r
        k=k//10
    if sum==i:
        rg=i
        break
c=temp-le
d=rg-temp
if c<d:
    print(le)
elif d<c:
    print(rg)
else:
    print(le,rg,end=" ")