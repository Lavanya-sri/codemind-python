n=input()
s=n.split()
c=0
for words in s:
    x=words.lower()
    v=x[::-1]
    if v==x:
        c+=1
print(c)