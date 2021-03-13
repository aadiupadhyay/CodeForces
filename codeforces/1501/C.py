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
    d = {}
    l = li()
    for i in range(n):
        for j in range(i+1, n):
            s = l[i]+l[j]
            if s not in d:
                d[s] = [i, j]
            elif (i not in d[s]) and (j not in d[s]):
                pr('YES')
                print(i+1, j+1, d[s][0]+1, d[s][1]+1)
                return
    pr('NO')


solve()
