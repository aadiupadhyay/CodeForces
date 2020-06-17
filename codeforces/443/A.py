def solve():
    s=input()
    l=[]
    c=0
    n=len(s)
    for i in range(n):
        if i==0 or i==n-1 or s[i]=="," or s[i]==" ":
            continue
        else:
            if s[i] not in l:
                l.append(s[i])
                c+=1
    print(c)
solve()
