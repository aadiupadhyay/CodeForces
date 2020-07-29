s=input()
if len(s)&1:
    print("No")
else:
    d={}
    c=0
    for i in s:
        d[i]=d.get(i,0)+1
    for i in d:
        if d[i]&1:
            c=1
            break
    if c:
        print("No")
    else:
        print("Yes")
