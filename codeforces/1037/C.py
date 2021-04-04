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
    a = input()
    b = input()
    ans = 0
    i = 0
    while i < n:
        if a[i] == b[i]:
            i += 1

        elif i+1 < n:
            if a[i] != b[i] and a[i+1] != b[i+1] and a[i] != a[i+1]:
                ans += 1
                i += 2
            else:
                ans += 1
                i += 1
        else:
            if a[i] != b[i]:
                ans += 1
                i += 1
    pr(ans)


for _ in range(1):
    solve()
