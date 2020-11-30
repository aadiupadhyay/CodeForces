from sys  import stdin,stdout
from collections  import *
from math import gcd,floor,ceil
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

def solve():
    n,x = mp()
    l=li()
    ans=0
    i=0
    while i<n:
        if l==sorted(l):
            pr(ans)
            return 
        if l[i]>x:
            x,l[i]=l[i],x
            ans+=1
        i+=1
    pr(-1)
        
            
    
for _ in range(inp()):
    solve()
