n=int(input())
x=0
for i in range(1,n-1):
    if n==i*(i+1):
        x+=1
if x==1:
     print("YES")
else:
    print("NO")