from sys  import stdin,stdout
from collections  import *
from math import ceil, floor , log, gcd
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")
 
mod=1000000007
INF=float('inf')

def solve():
    n,k=mp()
    s=st()
    if s.count('W')==0:
        print(max(0,2*k -1))
        return
    ans=0
    W=0
    cur=0
    w=0
    x=[]
    for i in range(n):
        if s[i]=='W':
            if cur:
                x.append(cur)
                cur=0
            ans+=1
            w+=1
            if W:
                ans+=1
            W=1
        else:
            W=0
            if w:
                cur+=1
    k=min(k,n-w)
    ans+= 2*k
    x.sort()
    for i in x:
        if i<=k:
            ans+=1
            k-=i
    pr(ans)
            
        
            
        
    
    
for _ in range(inp()):
    solve()
