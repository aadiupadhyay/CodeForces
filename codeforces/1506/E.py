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


def solve():

    def update(ind):
        ind += n
        segment[ind] = -INF
        while ind > 1:
            ind >>= 1
            segment[ind] = max(segment[2*ind], segment[2*ind+1])

    def getMax(a, b):
        a += n
        b += n
        s = -INF
        while a <= b:
            if a % 2:
                s = max(s, segment[a])
                a += 1
            if b % 2 == 0:
                s = max(s, segment[b])
                b -= 1
            b >>= 1
            a >>= 1
        update(s-1)
        return s

    n = inp()
    l = li()
    ma = [0]
    segment = [0]
    ans1 = []
    for i in range(n):
        ma.append(0)
        segment.append(0)
        ans1.append(0)

    segment = segment + segment
    for i in range(n):
        segment[i+n] = i+1

    for i in range(n-1, 0, -1):
        segment[i] = max(segment[2*i], segment[2*i+1])
    ans2 = list(ans1)
    ma[l[0]] = 1
    ans1[0] = l[0]
    ans2[0] = l[0]
    i = 1
    update(l[0]-1)
    while i < n:
        if l[i] > l[i-1]:
            ma[l[i]] = 1
            update(l[i]-1)
            ans2[i] = l[i]
            ans1[i] = l[i]

        i += 1
    j = 1

    for i in range(n):
        if ans1[i] == 0:
            while j < n and ma[j] == 1:
                j += 1
            ans1[i] = j
            ma[j] = 1
    for i in range(n):
        if ans2[i] != 0:
            now = ans2[i]
        elif ans2[i] == 0:
            last = getMax(0, now-1)
            ans2[i] = last

    print(*ans1)
    print(*ans2)


for _ in range(inp()):
    solve()
