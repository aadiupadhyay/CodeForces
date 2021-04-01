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

dp = [2]
i = 2
while dp[-1] <= 10**9:
    dp.append(i*2+i-1+dp[-1])
    i += 1


def solve():
    def Binary_Search(x):
        i = 0
        j = len(dp)-1
        while j-i > 1:
            mid = (i+j)//2
            if dp[mid] <= x:
                i = mid
            else:
                j = mid
        return i
    n = inp()
    ans = 0
    while n >= 2:
        a = Binary_Search(n)
        n -= dp[a]
        ans += 1
    pr(ans)


for _ in range(inp()):
    solve()
