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
    n=inp()
    l=li()
    d=defaultdict(int)
    for i in range(1,n):
        if l[i]!=l[i-1]:
            d[l[i]]+=1
    for i in d:
        if i!=l[-1]:
            d[i]+=1
    if not d:
        pr(0)
        return 
    if d[l[0]]==0:
        pr(1)
        return 
    pr(min(d.values()))
        
            
    
for _ in range(inp()):
    solve()
