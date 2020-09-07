def union(x,y):
    par[x]+=par[y]
    par[y]=x
    


def find(a):
    ans=[]
    while par[a]>=0:
        ans.append(a)
        a=par[a]
    for i in ans:
        par[i]=a
    return a



n,q=map(int,input().split())
par={i:-1 for i in range(n)}
for _ in range(q):
    a,b,c=map(int,input().split())
    if a==0:
        x,y=find(b),find(c)
        if x!=y:
            union(x,y)
    else:
        x,y=find(b),find(c)
        if x==y:
            print('1')
        else:
            print('0')
    
        
