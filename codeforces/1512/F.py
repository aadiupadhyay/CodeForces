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
    a = li()
    b = li()
    b.append(0)
    ans = INF
    total = 0
    day = 0
    for i in range(n):
        if total >= k:
            pr(ans)
            return
        if i == n-1:
            p = k - total
            h = (p+a[i]-1)//a[i]
            ans = min(ans, day+h)
        else:
            p = k - total
            h = (p+a[i]-1)//a[i]
            ans = min(ans, day+h)
            if total >= b[i]:
                day += 1
                total -= b[i]
            else:
                u = (b[i]-total + a[i]-1)//a[i]
                day += u+1
                total = total + a[i]*u - b[i]
    pr(ans)


for _ in range(inp()):
    solve()
