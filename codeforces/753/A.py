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


n = inp()
if n == 1 or n == 2:
    pr(1)
    pr(n)
else:
    cur = 1
    r = n
    ans = []
    while cur < n-(cur*(cur+1)//2):
        ans.append(cur)
        cur += 1
    ans.append(n-(cur*(cur-1)//2))
    print(len(ans))
    print(*ans)
