n=input()
l=len(n)
n=int(n)
x=n
sum=0
while(n):
    r=n%10
    sum=sum+pow(r,l)
    l=l-1
    n=n//10
if x==sum:
    print("True")
else:
    print("False")
