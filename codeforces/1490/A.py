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
    n=inp()
    l=li()
    ans=0
    for i in range(1,n):
        if max(l[i],l[i-1]) >= 2*min(l[i],l[i-1]):
            x= min(l[i],l[i-1])
            while 2*x <max(l[i],l[i-1]):
                ans+=1
                x*=2
    pr(ans)
 
 
for _ in range(inp()):
    solve()