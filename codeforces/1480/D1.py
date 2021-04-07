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
x, y = 0, 0
ans = 0
for j in range(n):
    i = l[j]
    if i != x and i != y:
        if j+1 < n:
            if l[j+1] == x:
                x = i
            elif l[j+1] == y:
                y = i
            else:
                x = i
            ans += 1
        else:
            ans += 1
            x = i

    elif i != y:
        y = i
        ans += 1
    elif i != x:
        x = i
        ans += 1
print(ans)
