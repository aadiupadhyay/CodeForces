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
    l = [li() for i in range(n)]
    x = li()
    z = 0
    for i in range(n-1):
        arrived = l[i][0]+x[i]+z
        p = arrived+ceil((l[i][1]-l[i][0])/2)
        if p < l[i][1]:
            left = l[i][1]
        else:
            left = p
        if left - l[i][1] < 0:
            z = 0
        else:
            z = left - l[i][1]
    pr(l[-1][0]+z+x[-1])


for _ in range(inp()):
    solve()
