# aadiupadhyay
import sys
from collections import *
import os.path
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
    n = inp()
    l = li()
    pref_pos = [0 for i in range(n)]
    suf_neg = [0 for i in range(n)]
    a, b = INF, -INF
    for i in range(n):
        if l[i] >= 0:
            if i == 0:
                pref_pos[i] = 1
            else:
                pref_pos[i] = 1+pref_pos[i-1]
        else:
            if i != 0:
                pref_pos[i] += pref_pos[i-1]
        if l[n-i-1] <= 0:
            if i == 0:
                suf_neg[n-i-1] = 1
            else:
                suf_neg[n-1-i] = 1+suf_neg[n-i]
        else:
            if i != 0:
                suf_neg[n-i-1] += suf_neg[n-i]
        a = min(a, l[i])
        b = max(b, l[i])

    if (a > 0 and b > 0) or (a < 0 and b < 0):
        pr(1)
        return
    ans = INF
    # print(pref_pos)
    # print(suf_neg)
    for i in range(n-1):
        ans = min(ans, pref_pos[i]+suf_neg[i+1])
    pr(ans)


solve()
