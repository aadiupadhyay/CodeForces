from sys import stdin, stdout
from collections import *
from math import gcd, floor, ceil
def st(): return list(stdin.readline().strip())
 
 
def li(): return list(map(int, stdin.readline().split()))
def mp(): return map(int, stdin.readline().split())
def inp(): return int(stdin.readline())
def pr(n): return stdout.write(str(n)+"\n")
 
 
mod = 1000000007
INF = float('inf')
 
 
def solve():
    def hii(l,x):
        if not l:
            return 
        a=max(l)
        d[a]=x+1
        p  =l.index(a)
        hii(l[:p],x+1)
        hii(l[p+1:],x+1)
    d= defaultdict()
    n=inp()
    l=li()
    hii(l,-1)
    for i in l:
        print(d[i],end=' ')
    print()
    
for _ in range(inp()):
    solve()