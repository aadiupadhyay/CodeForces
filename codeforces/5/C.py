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
n = len(s)
valid = [-1]*n
freq = [0]*(n+1)
stack = []
for i in range(n):
    if s[i] == ')':
        if stack:
            last = stack.pop()
            if last - 1 >= 0 and valid[last-1] != -1:
                last = valid[last-1]
            valid[i] = last
            now = i - last + 1
            freq[now] += 1
    else:
        stack.append(i)
g = 0
for i in range(n, 0, -1):
    if freq[i] > 0:
        print(i, freq[i])
        g = 1
        break
if g == 0:
    print(0, 1)
