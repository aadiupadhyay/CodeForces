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
    l = li()
    ma = [0 for i in range(n+1)]
    mi = list(ma)
    ans1 = [0 for i in range(n)]
    ans2 = list(ans1)
    ma[l[0]] = 1
    mi[l[0]] = 1
    ans1[0] = l[0]
    ans2[0] = l[0]
    i = 1
    while i < n:
        if l[i] > l[i-1]:
            ma[l[i]] = 1
            mi[l[i]] = 1
            ans2[i] = l[i]
            ans1[i] = l[i]
        i += 1
    j = 1

    for i in range(n):
        if ans1[i] == 0:
            while j < n and ma[j] == 1:
                j += 1
            ans1[i] = j
            ma[j] = 1
    for i in range(n):
        if ans2[i] == 0:
            last = ans2[i-1]
            while mi[last] == 1 and last > 0:
                last -= 1
            ans2[i] = last
            mi[last] = 1

    print(*ans1)
    print(*ans2)


for _ in range(inp()):
    solve()
