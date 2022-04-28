n=input()
len_n=len(n)
n=int(n)
x=n
i=len_n
add=0
while n!=0:
    r=n%10
    add=add+(r**i)
    n=n//10
    i=i-1
if add==x:
    print("True")
else:
    print("False")
    