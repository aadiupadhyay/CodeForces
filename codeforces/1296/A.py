for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    o,e=0,0
    for i in l:
        if i&1:
            o+=1
        else:
            e+=1
    if n&1:
        if e==n:
            print("NO")
        else:
            print("YES")
    else:
        if o==0 or o==n:
            print("NO")
        else:
            print("YES")
