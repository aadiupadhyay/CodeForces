n=int(input())
s=input()
x=""
if n&1:
    for i in range(3):
        x+=s[i]
    for i in range(3,n,2):
        x+="-"+s[i]+s[i+1]
else:
    for i in range(0,n,2):
        x+=s[i]+s[i+1]+"-"
    x=x[:-1]
print(x)
