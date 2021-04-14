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


s = st()
a, b = 0, 0
x = set()
f = 0
for i in s:
    x.add((a, b))
    if i == 'U':
        a -= 1
    if i == 'D':
        a += 1
    if i == 'L':
        b -= 1
    if i == 'R':
        b += 1
    if (a, b) in x:
        f = 1
        break
    c = 0
    if (a-1, b) in x:
        c += 1
    if (a+1, b) in x:
        c += 1
    if (a, b-1) in x:
        c += 1
    if (a, b+1) in x:
        c += 1
    if c > 1:
        f = 1
        break
pr('OK' if f == 0 else 'BUG')
