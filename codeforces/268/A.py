def solve():
    n=int(input())
    l=[]
    k=[]
    c=0
    for i in range(n):
        a,b=map(int,input().split())
        l.append(a)
        k.append(b)
    for i in range(n):
        c+=k.count(l[i])
        l[i]=0
    for i in range(n):
        c+=l.count(k[i])
        k[i]=0
    print(c)
            
    

solve()
