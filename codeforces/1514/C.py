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


n = inp()
i = 2
s = set(range(1, n))
f = []
while i*i <= n:
    if n % i == 0:
        f.append(i)
        if i != n//i:
            f.append(n//i)
    i += 1
c = 1
for i in f:
    for j in range(i, n, i):
        s.discard(j)
for i in s:
    c = (c*i) % n
if c != 1:
    s.discard(max(s))
a = list(s)
pr(len(a))
print(*sorted(a))
