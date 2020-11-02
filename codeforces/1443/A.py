from sys  import stdin,stdout
from collections  import *
from math import gcd,floor,ceil
from bisect import bisect_left as bl
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

INF=float('inf')
mod=1000000007

def solve():
    n=inp()
    val=4*n
    cur=[]
    for _ in range(n):
        cur.append(val)
        val-=2
    pr(' '.join(map(str,cur)))
        
    
    
for _ in range(inp()):
    solve()
