num = int(input())  
x=len(str(num))  
square = num**2  
last_digits = square%pow(10,x)  
if last_digits == num:  
  print("Automorphic Number")  
else:  
  print("Not an Automorphic Number") 