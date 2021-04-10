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
    ind = []
    l = []
    for i in range(n):
        s = st()
        l.append(s)
        for j in range(n):
            if s[j] == '*':
                ind.append((i, j))
    A, B = ind
    x, y = A
    a, b = B
    if x == a:
        if x+1 < n:
            l[x+1][y] = '*'
            l[x+1][b] = '*'
        else:
            l[x-1][y] = '*'
            l[x-1][b] = '*'
    elif y == b:
        if y+1 < n:
            l[x][y+1] = '*'
            l[a][y+1] = '*'
        else:
            l[x][y-1] = '*'
            l[a][y-1] = '*'
    else:
        l[x][b] = '*'
        l[a][y] = '*'
    for i in l:
        print(*i, sep='')


for _ in range(inp()):
    solve()
