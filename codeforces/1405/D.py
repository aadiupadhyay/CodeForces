from __future__ import print_function
range = xrange
input = raw_input

def Diameter(x):
    v[x]=True
    stack=[x]
    while stack:
        a=stack.pop()
        for  i in d[a]:
            if not v[i]:
                v[i]=True
                stack.append(i)
                dis[i]=dis[a]+1


def BFS(a):
    v[a]=True
    q=[a]
    while q:
        p=q.pop(0)
        for i in d[p]:
            if not v[i]:
                q.append(i)
                v[i]=True
                distance[i]=distance[p]+1
        

for _ in range(int(input())):
    n,a,b,da,db=map(int,input().split())
    d={i:[] for i in range(1,n+1)}
    for i in range(n-1):
        x,y=map(int,input().split())
        d[x].append(y)
        d[y].append(x)

    dis=[0 for i in range(n+1)]
    v=[False for i in range(n+1)]
    Diameter(1)

    ans=float('-inf')
    for i in range(len(dis)):
        if dis[i]>ans:
            ans=dis[i]
            node=i
            
    dis=[0 for i in range(n+1)]
    v=[False for i in range(n+1)]

    Diameter(node)
    dia=float('-inf')
    for i in range(len(dis)):
        if dis[i]>dia:
            dia=dis[i]
        

    distance=[0 for i in range(n+1)]
    v=[False for i in range(n+1)]
    BFS(a)

    if distance[b]>da and 2*da < dia and db>2*da:
        print('Bob')
    else:
        print('Alice')
