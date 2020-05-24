s=input()
ss=input()
x=""
for i in range(len(s)):
    if s[i]!=ss[i]:
        x+="1"
    else:
        x+="0"
print(x)
