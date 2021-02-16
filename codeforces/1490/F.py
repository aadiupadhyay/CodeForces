
from sys import stdin, stdout
from collections import *
from math import gcd, floor, ceil
from bisect import bisect_right
def st(): return list(stdin.readline().strip())


def li(): return list(map(int, stdin.readline().split()))
def mp(): return map(int, stdin.readline().split())
def inp(): return int(stdin.readline())
def pr(n): return stdout.write(str(n)+"\n")


mod = 1000000007
INF = float('inf')


def solve():
    n=inp()
    l=li()
    d=Counter(l)
    x=list(d.values())
    x.sort(reverse= True)
    ans= INF 
    s=0
    tot = n
    for i in range(len(x)):
        val = tot  - i*x[i] -x[i]
        ans = min(ans,val)
        s+=x[i]
    pr(ans)

for _ in range(inp()):
    solve()
