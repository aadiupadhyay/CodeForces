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
    d=Counter(l)
    for i in range(n):
        a=l[i]^x
        ans+=d.get(a,0)
        if x==0:
            ans-=1
    pr(ans//2)

            
    
for _ in range(1):
    solve()
