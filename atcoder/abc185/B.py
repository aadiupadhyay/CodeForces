# cook your dish here
from sys import stdin, stdout
from collections import *
from math import gcd, floor, ceil
def st(): return list(stdin.readline().strip())


def li(): return list(map(int, stdin.readline().split()))
def mp(): return map(int, stdin.readline().split())
def inp(): return int(stdin.readline())
def pr(n): return stdout.write(str(n)+"\n")


mod = 1000000007
INF = float('inf')


def solve():
    n, m, t = mp()
    ans = n
    l = [li() for i in range(m)]
    prev = 0
    for i in l:
        a, b = i
        ans -= (a-prev)
        if ans <= 0:
            pr('No')
            return
        else:
            ans += b-a
            prev = b
        if ans >= n:
            ans = n
    if ans <= t-prev:
        pr('No')
        return
    print('Yes')


for _ in range(1):
    solve()
