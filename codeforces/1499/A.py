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
    n, k1, k2 = mp()
    w, b = mp()
    cur = 2*n - k1 - k2
    if w << 1 <= k1+k2 and b << 1 <= cur:
        pr('YES')
    else:
        pr('NO')


for _ in range(inp()):
    solve()
