# aadiupadhyay
# started 5 min late
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
    x = li()
    occ = defaultdict(int)
    for i in range(n):
        if not occ[l[i]]:
            occ[l[i]] = i+1
    ans = []
    for i in x:
        ans.append(occ[i])
        if occ[i] == 1:
            continue
        for j in occ:
            if occ[j] < occ[i]:
                occ[j] += 1
        occ[i] = 1

    print(*ans)


for _ in range(1):
    solve()
