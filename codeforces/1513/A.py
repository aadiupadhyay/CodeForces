# aadiupadhyay
from decimal import *
import sys
from collections import *
import os.path
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
    l = list(range(1, n+1))
    for i in range(1, n, 2):
        if i+1 == n:
            break
        if k:
            l[i], l[i+1] = l[i+1], l[i]
            k -= 1
    if k == 0:
        print(*l)
    else:
        pr(-1)


for _ in range(inp()):
    solve()
