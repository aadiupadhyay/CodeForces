a="abcdefghijklmnopqrstuvwxyz"
b=a.upper()
s=input()
c,d=0,0
for i in s:
    if i in a:
        c+=1
    else:
        d+=1
if d>c:
    print(s.upper())
else:
    print(s.lower())