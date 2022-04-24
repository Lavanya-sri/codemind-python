n=int(input())
count=0
r=0
while n!=0:
    r=n%10
    count=count*10+r
    n=n//10
print(count)