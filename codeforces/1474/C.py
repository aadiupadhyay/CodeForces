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
    def check(a, x, ans):
        d = defaultdict(list)
        for i in range(len(a)):
            d[a[i]].append(i)
        for i in a:
            if i in d:
                d[i].pop()
                if not d[i]:
                    del d[i]
                y = x - i
                if y not in d:
                    return False, []
                ans.append([i, y])
                d[y].pop()
                if not d[y]:
                    del d[y]
                x = i
        return True, ans
    n = inp()*2
    l = li()
    l.sort(reverse=True)
    for i in range(1, n):
        a, b = check(l[1:i]+l[i+1:], l[0], [])
        if a:
            pr('YES')
            print(l[i]+l[0])
            print(l[i], l[0])
            for i in b:
                print(*i)
            return
    pr('NO')


for _ in range(inp()):
    solve()
