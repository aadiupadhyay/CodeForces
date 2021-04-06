# aadiupadhyay
import sys
from collections import *
from random import *
import os.path
from math import gcd
mod = 998244353
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
    def valid(m, s):
        return s >= 0 and s <= 9*m

    m, s = mp()
    if s == 0 and m == 1:
        print("0 0")
    elif s == 0 or s > 9*m:
        print("-1 -1")
    else:
        mins = ''
        maxs = ''
        x = s
        y = s
        for i in range(m):
            for j in range(10):
                if i == 0 and j == 0:
                    continue
                if valid(m-i-1, x-j):
                    x -= j
                    mins += str(j)
                    break
            for j in range(9, -1, -1):
                if valid(m-i-1, y-j):
                    y -= j
                    maxs += str(j)
                    break
        print(mins, maxs)


for _ in range(1):
    solve()
