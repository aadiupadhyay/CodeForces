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

def optimal_summands(n):


    summands = [] # array to store pairwise distinct positive integers
    k = n # marked the upper part
    m = 1 # marked the lower part

    if n == 2 or n == 1:
        summands.append(n)
    else:
        for i in range(1,k):
            if k <= 2*m:
                summands.append(k)
                break
            else:
                summands.append(m)
                k = k - m
                m = m + 1

    return summands

n = inp()
ans = optimal_summands(n)
print(len(ans))
print(*ans)
