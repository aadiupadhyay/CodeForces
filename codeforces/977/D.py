from sys  import stdin,stdout
from collections import deque

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007

def solve():
    n=inp()
    l=li()
    d={i:[] for i in l}
    m=max(d)
    for i in range(n):
        if 2*l[i] <= m:
            if 2*l[i] in l:
                d[l[i]].append(2*l[i])
        if l[i]%3==0:
            if l[i]//3 in l:
                d[l[i]].append(l[i]//3)
   
    for i in l:
        q=deque()
        v=set()
        par={i:-1 for i in l}
        q.append(i)
        ans=[i]
        v.add(i)
        while q:
            a=q.popleft()
            for i in d[a]:
                par[i]=a
                q.append(i)

        if list(par.values()).count(-1)==1:
            dd={}
            for i in par:
                dd[par[i]]=i
            
            x=dd[-1]
            print(x,end=' ')
            for i in range(n-1):
                print(dd[x],end=' ' )
                x=dd[x]
                
            
            
        
        
        
            

for _ in range(1):
    solve()
