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
    n, m = mp()
    l = []
    up = []
    down = []
    left = []
    right = []
    zero = [0]*m
    for i in range(n):
        x = li()
        l.append(x)
        up.append(list(zero))
        down.append(list(zero))
        left.append(list(zero))
        right.append(list(zero))
        left[i][0] = x[0]
        right[i][-1] = x[-1]
        for j in range(1, m):
            left[i][j] = x[j]+left[i][j-1]
            right[i][m-1-j] = x[m-1-j] + right[i][m-j]
    for i in range(m):
        up[0][i] = l[0][i]
        down[-1][i] = l[-1][i]
        for j in range(1, n):
            up[j][i] = l[j][i] + up[j-1][i]
            down[n-j-1][i] = l[n-1-j][i] + down[n-j][i]
    ans = 0
    for i in range(n):
        for j in range(m):
            if l[i][j] != 1:
                c = 0
                c += min(1, up[i][j])
                c += min(1, down[i][j])
                c += min(1, left[i][j])
                c += min(1, right[i][j])
                ans += c

    pr(ans)


for _ in range(1):
    solve()
