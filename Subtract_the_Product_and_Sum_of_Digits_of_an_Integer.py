n=int(input())
p=1
sum=0
while n>0:
    r=n%10
    sum=sum+r
    p=p*r
    n=n//10
c=p-sum
print(c)