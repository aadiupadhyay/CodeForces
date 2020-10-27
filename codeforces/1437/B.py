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
    n=inp()
    s=st()
    ans=0
    for i in range(n-1):
        if s[i]==s[i+1]:
            ans+=1
    pr(ceil(ans/2))
    
for _ in range(inp()):
    solve()
