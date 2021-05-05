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


n, t = mp()
k = inp()
low = 1
high = n
while low <= high:
    mid = (low+high)//2
    print('?', 1, mid, flush=True)
    val = inp()
    if (mid-val) >= k:
        high = mid-1
    else:
        low = mid+1
print('!', low, flush=True)