def ispngrm(str):
    x='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for ch in x:
        if ch not in str.upper():
           return False
    return True
    



str=input()
if ispngrm(str):
    print("True")
else:
    print("False")