from sys  import stdin,stdout
from collections import *

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF= float('inf')


def solve():
    n=inp()
    l=li()
    x=max(l)
    y=min(l)
    if x==y:
        pr(-1)
        return
    for i in range(1,n):
        if l[i]==x and l[i-1]<x:
            pr(i+1)
            return
    for i in range(n-1):
        if l[i]==x and l[i+1]<x:
            pr(i+1)
            return
    pr(-1)
            
        
        
    
    
    
        

for _ in range(inp()):

    solve()

