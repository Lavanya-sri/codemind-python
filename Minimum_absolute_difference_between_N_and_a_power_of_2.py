n=int(input())
l=2
r=2
while l*2<=n:
    l=l*2
r=l*2
if n-l<r-n:
    print(n-l)
elif n-l==r-n:
    print(l,r,end=" ")
else:
    print(r-n)