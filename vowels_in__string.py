n=input()
a=[]
for i in n:
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'or i=='A'or i=='E'or i=='I'or i=='O'or i=='U') and i not in a:
        a.append(i)
        print(i,end=" ")