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
    n, k = mp()
    l = li()
    l.sort()
    s = sum(l)
    if s == k:
        pr('NO')
        return
    ind = -1
    ans = []
    x = 0
    for i in range(n):
        if x+l[i] == k:
            ind = i
        else:
            ans.append(l[i])
            x += l[i]
    if ind != -1:
        ans.append(l[ind])
    pr('YES')
    print(*ans)


for _ in range(inp()):
    solve()
