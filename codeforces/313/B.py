# aadiupadhyay
import os.path
from math import gcd, floor, ceil
from collections import *
from bisect import *
import sys
from random import *
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
n = len(s)
m = inp()
l = [li() for i in range(m)]
ans = [0 for i in range(n+1)]
for i in range(1, n):
    ans[i] = ans[i-1]
    if s[i-1] == s[i]:
        ans[i] += 1
ans[-1] = ans[-2]
for i in l:
    print(ans[i[1]-1]-ans[i[0]-1])
