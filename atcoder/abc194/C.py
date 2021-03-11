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
l = li()
ans = 0
pre_sum = l[0]
pre_sum_sq = l[0]*l[0]
for i in range(1, n):
    ans += i*(pow(l[i], 2)) + pre_sum_sq - 2*l[i]*pre_sum
    pre_sum += l[i]
    pre_sum_sq += l[i]*l[i]
pr(ans)
