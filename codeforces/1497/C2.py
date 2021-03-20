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
    n -= (k-3)
    if n & 1:
        print(n//2, n//2, 1, end=' ')
    else:
        if n % 4 == 0:
            print(n//4, n//4, n//2, end=' ')
        else:
            print(2, n//2-1, n//2-1, end=' ')

    print(*[1 for i in range(k-3)])


for _ in range(inp()):
    solve()
