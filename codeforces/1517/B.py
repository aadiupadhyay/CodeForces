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
    ans = []
    n, m = mp()
    l = []
    cur = [0 for i in range(m)]
    for i in range(n):
        x = li()
        x.sort()
        ans.append(list(cur))
        l.append(x)
    for i in range(m):
        mi = INF
        for j in range(n):
            if l[j][0] < mi:
                mi = l[j][0]
                ind = j
        ans[ind][i] = mi
        l[ind].pop(0)
        for j in range(n):
            if j != ind:
                ans[j][i] = l[j][-1]
                l[j].pop()

    for i in ans:
        print(*i)


for _ in range(inp()):
    solve()
