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


def update(index, delta):
    while index <= n:
        BIT[index] += delta
        index += index & -index


def query(index):
    s = 0
    while index > 0:
        s += BIT[index]
        index -= index & -index
    return s


n = inp()
l = [0]+li()
x = sorted(l)
d = {x[i]: i for i in range(n+1)}
left = [0]
right = [0]
BIT = [0]
for i in range(n+1):
    l[i] = d[l[i]]
    left.append(0)
    right.append(0)
    BIT.append(0)
for i in range(1, n+1):
    update(l[i], 1)
    left[i] = query(n)-query(l[i])
BIT = [0 for i in range(n+2)]
for i in range(n, 0, -1):
    update(l[i], 1)
    right[i] = query(l[i]-1)
ans = 0
for i in range(1, n+1):
    ans += left[i]*right[i]
pr(ans)
