# aadiupadhyay
import sys
from collections import *
from random import *
import os.path
from math import gcd
mod = 998244353
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
    n = len(s)
    a1 = 0
    for i in range(1, n):
        if s[i] == s[i-1]:
            a1 += 1
            for j in 'abcdefghijklmnopqrstuvwxyz':
                if i+1 < n:
                    if s[i] != j and s[i+1] != j:
                        s[i] = j
                        break
                else:
                    if s[i] != j:
                        s[i] = j
                        break
    print(*s, sep='')


for _ in range(1):
    solve()
