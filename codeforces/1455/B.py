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
    a=1
    while a*(a+1)//2 < n:
        a+=1
    c=a*(a+1)//2 -n
    if c==1:
        pr(a+1)
    else:
        pr(a)
            
    
for _ in range(inp()):
    solve()