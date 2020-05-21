s=input()
a=["h","e","l","l","o"]
j=0
c=0
while j<5:
    if a[j] in s:
        x=s.index(a[j])
        s=s[x+1:]
    else:
        c=1
        break
    j+=1
if c==1:
    print("NO")
else:
    print("YES")
    
