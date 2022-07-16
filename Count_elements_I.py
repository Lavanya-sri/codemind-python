n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
m=0
x=set(a)
y=set(b)
for ele in x:
    if ele  in y:
        c+=1

print(c)