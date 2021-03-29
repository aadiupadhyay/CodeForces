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
    n, w = mp()
    l = li()
    C = Counter(l)
    ANS = 0
    while len(C) > 0:
        ANS += 1
        rest = w
        for i in range(30, -1, -1):
            while (1 << i) in C and rest >= (1 << i):
                rest -= (1 << i)
                C[(1 << i)] -= 1

                if C[1 << i] == 0:
                    del C[1 << i]
    pr(ANS)


for _ in range(inp()):
    solve()
