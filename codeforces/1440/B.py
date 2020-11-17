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
    n,k=mp()
    l=li()
    ans=0
    if n%2:
        x=n//2 +1
    else:
        x=n//2
    a=n-x+1
    b=0
    for i in range(len(l)-a,-1,-a):
        if b==k:
            break
        ans+=l[i]
        b+=1
    pr(ans)
        
 
     
for _ in range(inp()):
    solve()

