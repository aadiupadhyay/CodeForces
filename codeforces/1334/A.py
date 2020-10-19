
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
    p,q=0,0
    f=0
    for i in range(n):
        x,y = mp()
        if x<p or y<q or y-q > x-p:
            f=1
        p,q=x,y
    pr('YES' if f==0 else 'NO')

for _ in range(inp()):

    solve()

