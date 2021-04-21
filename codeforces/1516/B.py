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
    l = li()
    x = 0
    for i in l:
        x ^= i
    if not x:
        pr('YES')
        return
    i = 0
    a = 0
    while i < n:
        a ^= l[i]
        if a == x:
            break
        i += 1
    j = n-1
    b = 0
    while j >= 0:
        b ^= l[j]
        if b == x:
            break
        j -= 1
    if i+1 < j:
        pr('YES')
    else:
        pr('NO')


for _ in range(inp()):
    solve()
