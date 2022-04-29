n,r=map(int,input().split())
for i in range(1,r+1):
    if i%2==0:
        continue
    else:
        c=n*i
        print(n,'x',i,'=',c)
    i=i+1