# aadiupadhyay
# started 5 min late
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

    a, b, c = mp()
    cur = pow(10, c-1)
    x = cur
    while len(str(x)) < a:
        x *= 2
    y = cur
    while len(str(y)) < b:
        y *= 3
    print(x, y)


for _ in range(inp()):
    solve()
