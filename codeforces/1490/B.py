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
    x=[0,0,0]
    ans=0
    for i in l:
        x[i%3]+=1
    while len(set(x))>1:
        a=x.index(max(x))
        x[a]-=1
        x[(a+1)%3]+=1
        ans+=1
    pr(ans)
 
 
for _ in range(inp()):
    solve()