# aadiupadhyay
import os.path
from math import gcd, floor, ceil
from collections import *
import sys
from bisect import *
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
    a = li()
    b = li()
    x = [a[i]-b[i] for i in range(n)]
    x.sort()
    ans = 0
    for i in range(n):
        if x[i] <= 0:
            continue
        ind = bisect_left(x, -x[i]+1)
        ans += i - ind
    pr(ans)


for _ in range(1):
    solve()
