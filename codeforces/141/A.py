s=input()
ss=input()
sss=input()
s=s+ss
l=list(s)
k=list(sss)
l.sort()
k.sort()
if l==k:
    print("YES")
else:
    print("NO")
