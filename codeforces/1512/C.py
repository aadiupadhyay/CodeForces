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
    a, b = mp()
    s = st()
    n = a+b
    for i in range((n+1)//2):
        if s[i] == '?' or s[n-i-1] == '?':
            if s[i] == '?':
                s[i] = s[n-i-1]
            else:
                s[n-i-1] = s[i]
    p = [0, 0]
    for i in range(n):
        if s[i] != '?':
            p[int(s[i])] += 1
    for i in range((n+1)//2):
        if s[i] == '?' and s[n-i-1] == '?':
            cur = 1 + (i != (n-i-1))
            if p[0]+cur <= a:
                s[i] = s[n-i-1] = '0'
                p[0] += cur
            else:
                s[i] = s[n-i-1] = '1'
                p[1] += cur

    if p == [a, b] and s[::-1] == s:
        print(*s, sep='')
        return
    pr(-1)


for _ in range(inp()):
    solve()
