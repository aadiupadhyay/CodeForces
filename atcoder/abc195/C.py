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
power = 3
last = 1
ans = 0
while True:
    end = pow(10, power)-1
    if n > last and n > end:
        ans += (end-last+1)*(power//3-1)
        power += 3
        last = end+1
    else:
        ans += (n-last+1)*(power//3-1)
        break
print(ans)
