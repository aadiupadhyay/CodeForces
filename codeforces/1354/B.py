# aadiupadhyay
import os.path
from math import gcd, floor, ceil
from collections import *
from bisect import *
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
    def find(k):
        cur = [0, 0, 0, 0]
        for i in range(k):
            cur[int(s[i])] += 1
        if cur[1] and cur[2] and cur[3]:
            return True
        for i in range(k, n):
            cur[int(s[i-k])] -= 1
            cur[int(s[i])] += 1
            if cur[1] and cur[2] and cur[3]:
                return True
        return False

    s = st()
    n = len(s)
    a, b = s.count('1'), s.count('2')
    c = n-a-b
    if not a or not b or not c:
        pr(0)
        return
    low = 3
    high = n
    ans = -1
    while low <= high:
        mid = (low+high)//2
        if find(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid+1
    pr(ans)


for _ in range(inp()):
    solve()
