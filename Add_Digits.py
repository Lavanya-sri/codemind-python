n=int(input())
while(n>=10):
    temp=0
    while(n>0):
        temp=temp+n%10
        n=n//10
    n=temp
print(n)