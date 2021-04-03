# aadiupadhyay
import os.path
from math import gcd, floor, ceil
from collections import *
from bisect import *
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
    def ans(l, b, c):
        c -= 1
        b -= 1
        if b == 0:
            pr(l[c])
        else:
            pr(l[c]-l[b-1])
    n = inp()
    l = li()
    x = sorted(l)
    for i in range(1, n):
        x[i] += x[i-1]
        l[i] += l[i-1]
    for i in range(inp()):
        a, b, c = mp()
        if a == 1:
            ans(l, b, c)
        else:
            ans(x, b, c)


for _ in range(1):
    solve()
