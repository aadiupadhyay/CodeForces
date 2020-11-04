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
    l=li()
    k=li()
    n=inp()
    a,b=ceil(sum(l)/5),ceil(sum(k)/10)
    if a+b<=n:
        pr('YES')
    else:
        pr('NO')
  

for _ in range(1):
    solve()
