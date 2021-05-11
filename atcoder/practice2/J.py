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


def query(a, b):
    a += n
    b += n
    s = -INF
    while a <= b:
        if a & 1:
            s = max(seg[a], s)
            a += 1
        if b % 2 == 0:
            s = max(s, seg[b])
            b -= 1
        a >>= 1
        b >>= 1
    return s


def update(ind, val):
    ind += n
    seg[ind] = val
    ind >>= 1
    while ind > 1:
        seg[ind] = max(seg[ind << 1], seg[(ind << 1)+1])
        ind >>= 1


n, q = mp()
ans = []
l = li()
seg = [0]*n + l
for i in range(n-1, 0, -1):
    seg[i] = max(seg[i << 1], seg[(i << 1) + 1])
for _ in range(q):
    x = li()
    type = x[0]
    if type == 1:
        index, value = x[1:]
        index -= 1
        update(index, value)
    elif type == 2:
        start, end = x[1:]
        start, end = start-1, end - 1
        ans.append(query(start, end))
    else:
        start, val = x[1:]
        start -= 1
        now = query(start, n-1)
        if now < val:
            ans.append(n+1)
        else:
            low = start
            high = n-1
            an = -1
            while low <= high:
                mid = (low+high) >> 1
                now = query(start, mid)
                if now >= val:
                    an = mid
                    high = mid - 1
                else:
                    low = mid + 1
            ans.append(an+1)
print(*ans, sep='\n')
