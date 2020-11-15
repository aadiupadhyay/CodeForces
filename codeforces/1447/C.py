from sys  import stdin,stdout
from collections  import *
from math import *
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

def solve():
    n,w= mp()
    l=li()
    ma = INF
    p = ceil(w/2)
    for i in range(n):
        if l[i]>=p and l[i]<=w:
            pr(1)
            pr(i+1)
            return
        ma=min(ma,l[i])
    if ma >w:
        pr(-1)
        return
    x=[[l[i],i+1] for i in range(n)]
    x.sort(reverse=True)
    ans=[]
    i=0
    s=0
    pre=[]
    while i<n:
        s+=x[i][0]
        pre.append(x[i][0])
        ans.append(x[i][1])
        if s>=p and s<=w:
            pr(len(ans))
            print(*ans)
            return
        if s>w:
            s-=pre[-1]
            pre.pop()
            ans.pop()
        i+=1
    if s>=p and s<=w:
        print(len(ans))
        print(*ans)
    else:
        pr(-1)
            
        


    
        
    

for _ in range(inp()):
    solve()
