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
maxN = 200000 + 5
dp = [[0 for i in range(10)] for j in range(maxN+1)]
for i in range(10):
    dp[0][i] = 1

for i in range(1, maxN+1):
    for j in range(9):
        dp[i][j] = dp[i-1][j+1]
    dp[i][9] = (dp[i-1][0] % mod + dp[i-1][1] % mod) % mod


def solve():
    n, m = mp()
    ans = 0
    for i in str(n):
        a = int(i)
        ans = (ans % mod + dp[m][a] % mod) % mod
    pr(ans)


for _ in range(inp()):
    solve()
