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
    ans = 0
    dp = [[0]*7]
    for i in range(n):
        cur = [0 for j in range(7)]
        s = st()
        for j in range(7):
            cur[j] += (s[j] == '1') + dp[-1][j]
            ans = max(ans, cur[j])
        dp.append(cur)
    pr(ans)


for _ in range(1):
    solve()
