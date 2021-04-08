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

# testing


if os.path.exists('input.txt'):
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

n, a, b, c = mp()
dp = [-INF for i in range(n+1)]
if a <= n:
    dp[a] = 1
if b <= n:
    dp[b] = 1
if c <= n:
    dp[c] = 1
for i in range(1, n+1):
    if i-a >= 0:
        dp[i] = max(dp[i], 1+dp[i-a])
    if i-b >= 0:
        dp[i] = max(dp[i], 1+dp[i-b])
    if i-c >= 0:
        dp[i] = max(dp[i], 1+dp[i-c])
pr(dp[-1])
