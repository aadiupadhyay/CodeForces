def solve():
    n=int(input())
    l=list(map(int,input().split()))
    e,o=0,0
    x=[]
    y=[]
    for i in range(n):
        if l[i]&1:
            o+=1
            if not i&1:
                x.append(i)
        else:
            e+=1
            if i&1:
                y.append(i)
    if o>n//2 or e>(n-n//2):
        print("-1")
    else:
        if len(x)!=len(y):
            print("-1")
        else:
            print(len(x))
        
        
for _ in range(int(input())):

    solve()
