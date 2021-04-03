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
    def FUN(s, i):
        if i == n:
            return s == 0
        return FUN((s+l[i]) % 360, i+1) or FUN((s-l[i]) % 360, i+1)

    n = inp()
    l = [inp() for i in range(n)]
    if FUN(0, 0):
        pr('YES')
    else:
        pr('NO')


for _ in range(1):
    solve()
