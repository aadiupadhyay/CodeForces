s=input().lower()
ss=input().lower()
c=0
for i in range(len(s)):
    if s[i]>ss[i]:
        c=1
        break
    elif s[i]<ss[i]:
        c=2
        break
if c==0:
    print("0")
elif c==1:
    print("1")
else:
    print("-1")