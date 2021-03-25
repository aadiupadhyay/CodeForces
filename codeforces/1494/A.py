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
    s = st()
    n = len(s)
    x, y = 0, 0
    p, q = 0, 0
    if s[0] == s[-1]:
        pr('NO')
        return
    for i in range(n):
        if s[i] == s[0]:
            x += 1
            y += 1
        elif s[i] == s[-1]:
            x -= 1
            y -= 1
        else:
            x += 1
            y -= 1
        if x < 0:
            p = 1
        if y < 0:
            q = 1
    if p == q == 1:
        pr('NO')
        return
    if p == x == 0:
        pr('YES')
        return
    if q == y == 0:
        pr('YES')
        return
    pr('NO')


for _ in range(inp()):
    solve()
