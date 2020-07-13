for _ in range(int(input())):
    s=list(input())
    h=list(input())
    a,b=len(h),len(s)
    if a<b:
        print("NO")
    elif a==b:
        d={}
        c=0
        dd={}
        for i in s:
            d[i]=d.get(i,0)+1
        for i in h:
            dd[i]=dd.get(i,0)+1
        for i in d:
            if i  not in dd:
                c=1
                break
            if i in d:
                if d[i]!=dd[i]:
                    c=1
                    break
        if c:
            print("NO")
        else:
            print("YES")
    else:
        x=sorted(s)

        c=0
        for i in range(a-b+1):
            if sorted(h[i:i+b])==x:
                c=1
                break
        if c:
            print("YES")
        else:
            print("NO")
                
            
            
