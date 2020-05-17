s=input()
l=len(s)
i=0
d=0
while i<=l-7:
    x=s[i]
    if s[i:i+7]==7*x:
        d=1
        break
    i=i+1

if d==0:
    print("NO")
else:
    print("YES")
        
