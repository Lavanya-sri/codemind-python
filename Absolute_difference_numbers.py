n,x=map(int,input().split())
if n>=2*x:
    y=int(str(n)[0:x])
    z=int(str(n)[-x:])
    #print(z)
    a=abs(y-z)
    print(a)