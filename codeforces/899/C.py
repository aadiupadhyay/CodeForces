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
s = n*(n+1)//2
if s % 2 == 0:
    pr(0)
else:
    pr(1)
size = n//2
ans = []
prl(size)
s = s//2
for i in range(n, 0, -1):
    if i > s:
        continue
    if size*(size-1) // 2 <= (s-i):
        ans.append(i)
        s -= i
        size -= 1
print(*ans)
