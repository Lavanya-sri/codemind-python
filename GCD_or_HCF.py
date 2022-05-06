def gcd_fun(x,y):
    if(y==0):
        return x
    else:
        return gcd_fun(y,x%y)
x,y=map(int,input().split())
num=gcd_fun(x,y)
print(num)