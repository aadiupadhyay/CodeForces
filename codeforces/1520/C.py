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
    dp = [[0]*n for i in range(n)]
    cur = 1
    i = 0
    while i < n:
        for j in range(i % 2, n, 2):
            dp[i][j] = cur
            cur += 1
        i += 1
    i = 1
    while i <= n:
        for j in range(i % 2, n, 2):
            dp[i-1][j] = cur
            cur += 1
        i += 1
    for i in range(n):
        for j in range(n):
            if i-1 >= 0 and abs(dp[i-1][j]-dp[i][j]) == 1:
                pr('-1')
                return
            if j-1 >= 0 and abs(dp[i][j-1]-dp[i][j]) == 1:
                pr('-1')
                return
            if i+1 < n and abs(dp[i+1][j]-dp[i][j]) == 1:
                pr('-1')
                return
            if j+1 <n and abs(dp[i][j+1]-dp[i][j]) == 1:
                pr('-1')
                return
    for i in dp:
        print(*i)


for _ in range(inp()):
    solve()