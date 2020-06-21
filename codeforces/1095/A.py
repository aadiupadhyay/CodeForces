n=int(input())
s=input()
x=""
i=-1
c=1
while i<n-c:
    i+=c
    c+=1
    x+=s[i]
print(x)
