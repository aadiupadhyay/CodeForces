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
    l = []
    n = inp()
    ans = INF
    for _ in range(n):
        s = input()
        l.append(s)
    for i in range(n):
        c = 0
        for j in range(n):
            if i != j:
                a = l[j]+l[j]
                b = a.find(l[i])
                if b == -1:
                    pr('-1')
                    return
                c += b
        ans = min(ans, c)
    pr(ans)


solve()
