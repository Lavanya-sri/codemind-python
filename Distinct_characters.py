s=input().lower()
a=""
s=s.replace(" ","")
for i in set(s):
    if s.count(i)==1:
        a+=i
a=list(a)
a.sort()
for i in a:
    print(i,end="")