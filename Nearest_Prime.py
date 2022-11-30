def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

for t in range(int(input())):
    n=int(input())
    temp=n
    l=0
    r=0
    for i in range(n,1,-1):
        if(prime(i)):
            l=i
            break
    for i in range(n+1,100000):
        if(prime(i)):
            r=i
            break
    c=temp-l
    d=r-temp
    if c<d:
        print(l)
    elif d<c:
        print(r)
    else:
        if r<l:
            print(r)
        else:
            print(l)