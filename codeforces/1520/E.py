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

# taken from leetcode


def solve():
    def minSwaps(nums, k):
        p = [i for i, v in enumerate(nums) if v == 1]
        # p[i]: the position of i-th 1
        n = len(p)
        presum = [0]*(n+1)
        # presum[i]: sum(p[0]...p[i-1])
        for i in range(n):
            presum[i+1] = presum[i]+p[i]

        res = INF

        # sliding window
        if k % 2 == 1:
            # if odd
            radius = (k-1)//2
            for i in range(radius, n-radius):
                # i-radius ... i ... i+radius
                # move radius to i
                # i+1, ..., i+radius
                right = presum[i+radius+1]-presum[i+1]
                # i-radius, ..., i-1
                left = presum[i]-presum[i-radius]
                res = min(res, right-left)
            return res-radius*(radius+1)
        else:
            # even
            radius = (k-2)//2
            for i in range(radius, n-radius-1):
                # i-radius ... i i+1 ... i+radius+1
                # move radius to i (moving to i+1 is also OK)
                # i+1, ..., i+radius+1
                right = presum[i+radius+2]-presum[i+1]
                # i-radius, ..., i-1
                left = presum[i]-presum[i-radius]
                res = min(res, right-left-p[i])
            return res-radius*(radius+1)-(radius+1)
    n = inp()
    s = st()
    l = []
    c = 0
    for i in range(n):
        if s[i] == '*':
            c += 1
            l.append(1)
        else:
            l.append(0)
    if c == 0:
        pr(0)
        return
    pr(minSwaps(l, c))


for _ in range(inp()):
    solve()