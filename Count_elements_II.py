n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
m=0
x=set(a)
y=set(b)
for ele in x:
    if ele not in y:
        c+=1
for ele in y:
    if ele not in x:
        c+=1
print(c)