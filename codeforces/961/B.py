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
    n, k = mp()
    l = li()
    x = li()
    ans = 0
    s = 0
    for i in range(n):
        if x[i] == 1:
            ans += l[i]
            l[i] = 0

    for i in range(k):
        s += l[i]
    now = s
    for i in range(k, n):
        s -= l[i-k]
        s += l[i]
        now = max(now, s)
    pr(ans+now)


for _ in range(1):
    solve()
