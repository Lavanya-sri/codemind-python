n=int(input())
l=[]
k=0
while n>0:
    r=n%10
    l.append(r)
    k=k+1
    n=n//10
for i in range(k-1,-1,-1):
    if l[i]==6:
        l[i]=9
        break
for i in range(k-1,-1,-1):
    print(l[i],end="")