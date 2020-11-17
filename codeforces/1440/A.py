from sys  import stdin,stdout
from collections  import *
from math import gcd,floor,ceil
from bisect import bisect_left as bl
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

def solve():
    n,a,b,h=mp()
    s=st()
    ans=0
    for i in range(n):
        x,y=INF,INF
        if s[i]=='0':
            x=a
            y=h+b
        else:
            x=b
            y=h+a
        ans+=min(x,y)
    pr(ans)
        
        
 
     
for _ in range(inp()):
    solve()

