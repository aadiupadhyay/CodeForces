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
    x, y = [], []
    s = 0
    for i in range(n):
        a, b = mp()
        x.append(a)
        y.append(b)
        s += a
    prefix = [0]
    suffix = [0]
    for i in range(n):
        prefix.append(max(prefix[-1], y[i]))
        suffix.append(max(suffix[-1], y[n-i-1]))
    suffix = suffix[::-1]
    ans = []
    for i in range(n):
        ans.append((s-x[i])*max(prefix[i], suffix[i+1]))
    print(*ans)


for _ in range(1):
    solve()
