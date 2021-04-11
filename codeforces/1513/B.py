# aadiupadhyay
from decimal import *
import sys
from collections import *
import os.path
mod = 1000000007
INF = float('inf')
def st(): return list(sys.stdin.readline().strip())
def li(): return list(map(int, sys.stdin.readline().split()))
def mp(): return map(int, sys.stdin.readline().split())
def inp(): return int(sys.stdin.readline())
def pr(n): return sys.stdout.write(str(n)+"\n")
def prl(n): return sys.stdout.write(str(n)+" ")


if os.path.exists('input.txt'):
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')


def solve():
    n = inp()
    l = li()
    d = Counter(l)
    x = l[0]
    for i in range(1, n):
        x &= l[i]
    cur = (d[x] % mod * (d[x]-1) % mod) % mod
    for i in range(1, n-1):
        cur = (cur % mod * i % mod) % mod
    pr(cur)


for _ in range(inp()):
    solve()
