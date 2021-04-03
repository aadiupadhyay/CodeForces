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


def fun(val, mm):
    for i in range(n):
        for j in range(n):
            if (i+j) % 2 == mm and dp[i][j] == 0:
                dp[i][j] = val
                print(val, i+1, j+1, flush=True)
                print()
                return 1
    return 0


n = inp()
cur = n*n
dp = [[0 for i in range(n)] for j in range(n)]
i, j = 1, 1
one = 0
while cur:
    x = inp()
    if cur == n*n:
        if x == 1:
            dp[0][0] = 3
        elif x == 2:
            dp[0][0] = 3
        else:
            dp[0][0] = 1
            one = 1
        print(dp[0][0], 1, 1, flush=True)
        print()
    else:
        if x == 1:
            if one == 1:
                c = fun(3, 1)
                if c == 0:
                    fun(2, 0)
            else:
                c = fun(3, 0)
                if c == 0:
                    fun(2, 1)
        elif x == 2:
            if one == 1:
                c = fun(1, 0)
                if c == 0:
                    fun(3, 1)

            else:
                c = fun(1, 1)
                if c == 0:
                    fun(3, 0)
        else:
            if one == 1:
                c = fun(1, 0)
                if c == 0:
                    fun(2, 1)
            else:
                c = fun(1, 1)
                if c == 0:
                    fun(2, 0)
    cur -= 1
