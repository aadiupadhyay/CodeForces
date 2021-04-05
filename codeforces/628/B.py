# aadiupadhyay
import sys
from collections import *
import os.path
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
    s = st()
    ans = 0
    n = len(s)
    for i in range(n):
        if int(s[i]) % 4 == 0:
            ans += 1
        if i+1 < n:
            a = int(s[i]+s[i+1])
            if a % 4 == 0:
                ans += i+1
    pr(ans)


solve()
