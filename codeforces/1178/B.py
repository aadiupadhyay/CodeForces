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
    def fun(x, i):
        c = 0
        if x == 'v':
            c -= 1
        j = i
        while j < n and s[j] == x:
            j += 1
            c += 1
        return c, j

    s = input()
    n = len(s)
    dp = []
    dp2 = []
    i = 0
    sum = 0
    while i < n:
        if s[i] == 'v':
            dp2.append(0)
        else:
            dp.append(0)
        x = s[i]
        p, i = fun(s[i], i)
        if x == 'v':
            sum += p
            dp.append(p)
        else:
            dp2.append(p)
    pre = 0
    ans = 0
    for i in range(len(dp)):
        if dp[i] == 0:
            ans += pre * dp2[i] * (sum-pre)
        else:
            pre += dp[i]
    pr(ans)


for _ in range(1):
    solve()
