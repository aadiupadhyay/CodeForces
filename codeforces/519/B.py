def solve():
    n=int(input())
    l=list(map(int,input().split()))
    k=list(map(int,input().split()))
    x=list(map(int,input().split()))
    d={}
    for i in l:
        d[i]=d.get(i,0)+1
    dd={}
    for i in k:
        dd[i]=dd.get(i,0)+1
    ddd={}
    for i in x:
        ddd[i]=ddd.get(i,0)+1
    for i in d:
        if i not in dd:
            print(i)
            break
        elif d[i]-dd[i]==1:
            print(i)
            break
    for i in dd:
        if i not in ddd:
            print(i)
            break
        elif dd[i]-ddd[i]==1:
            print(i)
            break
            
        
solve()
