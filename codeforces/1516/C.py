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
    def candivide(l):
        s = sum(l)
        if s % 2:
            return False
        s = s//2
        dp = [0 for i in range(s+1)]
        dp[0] = 1
        for i in l:
            for j in range(s, i-1, -1):
                dp[j] |= dp[j-i]
        return dp[-1]
    n = inp()
    l = li()
    if not candivide(l):
        pr(0)
        return
    ind = -1
    for i in range(n):
        if l[i] % 2:
            ind = i + 1
            break
    if ind != -1:
        pr(1)
        pr(ind)
        return
    f = 1
    for i in range(n):
        x = []
        for j in range(n):
            if i != j:
                x.append(l[j])
        if not candivide(x):
            pr(1)
            pr(i+1)
            return


solve()
