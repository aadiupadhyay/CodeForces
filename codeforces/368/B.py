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

n, m = mp()
l = li()
q = [inp() for i in range(m)]
s = {l[-1]}
ans = [0 for i in range(n)]
ans[-1] = 1
for i in range(n-2, -1, -1):
    ans[i] = ans[i+1]
    if l[i] not in s:
        s.add(l[i])
        ans[i] += 1
print(*[ans[i-1] for i in q], sep='\n')
