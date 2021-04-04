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
    l = li()
    x = [0, 0]
    ans = 0
    now = []
    for i in range(n):
        x[l[i] % 2] += 1
        if x[0] == x[1]:
            if i+1 != n:
                now .append(abs(l[i+1]-l[i]))
    now.sort()
    for i in now:
        if i > k:
            break
        k -= i
        ans += 1
    pr(ans)


for _ in range(1):
    solve()
