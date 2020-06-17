s=input()
l=input().split()
c=0
for i in l:
    if s[0]==i[0] or s[1]==i[1]:
        c=1
        break
if c==1:
    print("YES")
else:
    print("NO")
