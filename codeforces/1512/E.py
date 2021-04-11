# aadiupadhyay
import os.path
from math import gcd, floor, ceil
from collections import *
import sys
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
    n, a, b, total = mp()
    s = set(range(1, n+1))
    ele = b-a+1
    if total < ele*(ele+1)//2:
        pr(-1)
        return
    nsum = n*(n+1)//2
    left = n-ele
    leftsum = left*(left+1)//2
    have = nsum-leftsum
    if total > have:
        pr(-1)
        return
    cur = []
    i = n
    while total:
        w = total - i
        if w >= ele*(ele-1)//2:
            cur.append(i)
            total -= i
            s.discard(i)
            ele -= 1
        i -= 1
    l = []

    for i in range(a-1):
        p = max(s)
        s.discard(p)
        l.append(p)
    for i in range(b+1, n+1):
        p = max(s)
        s.discard(p)
        cur.append(p)
    l += cur
    print(*l)


for _ in range(inp()):
    solve()
