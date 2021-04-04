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
    l = []
    for i in range(n):
        x = st()
        x = list(map(int, x))
        l.append(x)

    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if l[i][j] == 1:
                c = 0
                if i == n-1 or j == n-1:
                    continue
                if i+1 < n:
                    if l[i+1][j] == 1:
                        c += 1
                if j+1 < n:
                    if l[i][j+1] == 1:
                        c += 1
                if c == 0:
                    pr('NO')
                    return
    pr('YES')


for _ in range(inp()):
    solve()
