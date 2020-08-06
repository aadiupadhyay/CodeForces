n=input()
c=0
d=0
for i in n:
    if i=="-":
        c=c+1
    else:
        d=d+1
if d==0 or c%d==0:
    print("YES")
else:
    print("NO")