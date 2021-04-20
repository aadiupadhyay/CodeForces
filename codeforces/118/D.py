# aadiupadhyay
import os.path
from math import gcd, floor, ceil
from collections import *
import sys
mod = 100000000
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

dp = {}


def fun(n1, n2, k1, k2):
    if (n1+n2) == 0:
        return 1

    if (n1, n2, k1, k2) in dp:
        return dp[(n1, n2, k1, k2)]

    x, y = 0, 0
    if n1 > 0 and k1 > 0:
        x = fun(n1-1, n2, k1-1, h2)
    if n2 > 0 and k2 > 0:
        y = fun(n1, n2-1, h1, k2-1)

    dp[(n1, n2, k1, k2)] = (x+y) % mod
    return dp[(n1, n2, k1, k2)]


n1, n2, h1, h2 = mp()
pr(fun(n1, n2, h1, h2))
