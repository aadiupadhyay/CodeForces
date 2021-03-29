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
    k -= 1
    ans = 1
    if k:
        ans = 2
    l = [1]*(n-1)
    while k:
        cur = 0
        for i in range(n-1):
            ans = (ans + l[i]) % mod
            cur = (cur + l[i]) % mod
            l[i] = cur
        l = l[::-1]
        k -= 1
    pr(ans)


for _ in range(inp()):
    solve()
