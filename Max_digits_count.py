n=int(input())
a=list(map(int,input().split()))
b=0
for i in a:
    i=abs(i)
    i=str(i)
    if len(i)>b:
        b=len(i)
c=0
for i in a:
    i=abs(i)
    i=str(i)
    if len(i)==b:
        c+=1
print(c)