# aadiupadhyay
import os.path
from math import gcd, floor, ceil
from collections import *
import sys
from heapq import *
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
    n, m, x = mp()
    ans = [0 for i in range(n)]
    l = li()
    p = [[l[i], i] for i in range(n)]
    p.sort(reverse=True)
    h = []
    dp = [0 for i in range(m)]
    for i in range(m):
        ans[p[i][1]] = i + 1
        heappush(h, (p[i][0], i+1))
        dp[i] += p[i][0]
    for i in range(m, n):
        a, b = heappop(h)
        dp[b-1] += p[i][0]
        ans[p[i][1]] = b
        heappush(h, (a+p[i][0], b))
    if max(dp) - min(dp) <= x:
        pr('YES')
        print(*ans)
        return
    pr('NO')


for _ in range(inp()):
    solve()
