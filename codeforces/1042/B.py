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
    d = defaultdict(lambda: INF)
    for i in range(n):
        a, s = input().split()
        a = int(a)
        s = ''.join(sorted(list(s)))
        d[s] = min(a, d[s])
    ans = INF
    ans = min(ans, d['A']+d['B']+d['C'])
    ans = min(ans, d['ABC'])
    ans = min(ans, d['A']+d['BC'])
    ans = min(ans, d['AB']+d['C'])
    ans = min(ans, d['AC']+d['B'])
    ans = min(ans, d['AC']+d['AB'])
    ans = min(ans, d['AB']+d['BC'])
    ans = min(ans, d['AC']+d['BC'])

    pr(ans if ans != INF else -1)


for _ in range(1):
    solve()
