
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
    x=[[l[i],i+1] for i in range(n)]
    x.sort()
    v=[0 for i in range(n)]
    p=list(v)
    p[0]=x[0][0]
    v[-1]=1
    for i in range(1,n):
        p[i]=p[i-1]+x[i][0]
    z=[x[-1][1]]
    c=1
    for i in range(n-2,-1,-1):
        if p[i]>=x[i+1][0] and v[i+1]:
            v[i]=1
            c+=1
            z.append(x[i][1])
        else:
            break
    z.sort()
    print(c)
    print(*z)
for _ in range(inp()):
    solve()
