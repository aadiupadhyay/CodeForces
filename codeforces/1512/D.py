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
    n = inp()
    l = li()
    l.sort()
    last = l[-1]
    s = sum(l)
    if s-l[-1]-l[-2] == l[-2]:
        print(*l[:n])
        return
    left = s-last
    for i in range(n+1):
        c = left - l[i]
        if c == last:
            ans = l[:i]+l[i+1:n+1]
            print(*ans)
            return
    pr(-1)


for _ in range(inp()):
    solve()
