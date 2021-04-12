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
    a = n*n - 4*n
    if a < 0:
        pr('N')
        return
    a = a**0.5
    x = (n + a)/2
    y = (n-a)/2
    z1 = n - x
    z2 = n - y
    if z1 >= 0 and x >= 0:
        print('Y', x, z1)
    elif z2 >= 0 and y >= 0:
        print('Y', z2, y)
    else:
        pr('N')


for _ in range(inp()):
    solve()
