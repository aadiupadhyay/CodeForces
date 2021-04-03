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
    a, b, c = mp()
    s = st()
    d = defaultdict(list)
    for i in range(n):
        d[s[i]].append(i)
    ans = [' ']*(n)
    i = 0
    sum = 0
    while i < len(d['S']) and a:
        ans[d['S'][i]] = 'R'
        a -= 1
        i += 1
        sum += 1
    i = 0
    while i < len(d['R']) and b:
        ans[d['R'][i]] = 'P'
        b -= 1
        i += 1
        sum += 1
    i = 0
    while i < len(d['P']) and c:
        ans[d['P'][i]] = 'S'
        c -= 1
        i += 1
        sum += 1
    if sum < (n//2+n % 2):
        pr('NO')
        return
    pr('YES')
    for i in range(n):
        if ans[i] == ' ':
            if a:
                ans[i] = 'R'
                a -= 1
            elif b:
                ans[i] = 'P'
                b -= 1
            else:
                ans[i] = 'S'
                c -= 1
    print(*ans, sep='')


for _ in range(inp()):
    solve()
