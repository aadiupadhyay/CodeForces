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
    n = inp()
    a = st()
    b = st()
    a = list(map(int, a))
    b = list(map(int, b))
    pref = []
    cur = [0, 0]
    for i in a:
        cur[i] += 1
        pref.append(list(cur))
    add = 0
    # print(pref)
    for i in range(n-1, -1, -1):

        if (a[i]+add) % 2 == b[i]:
            continue
        if pref[i][0] != pref[i][1]:
            pr('NO')
            return
        add += 1
    pr('YES')


for _ in range(inp()):
    solve()
