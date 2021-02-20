
from sys import stdin, stdout
from collections import *
def st(): return list(stdin.readline().strip())


def li(): return list(map(int, stdin.readline().split()))
def mp(): return map(int, stdin.readline().split())
def inp(): return int(stdin.readline())
def pr(n): return stdout.write(str(n)+"\n")


mod = 1000000007
INF = float('inf')


def solve():
    s = st()
    n = len(s)
    for i in range(n):
        if i % 2 == 0:
            if s[i] >= 'a' and s[i] <= 'z':
                continue
            else:
                pr('No')
                return
        else:
            if s[i] >= 'A' and s[i] <= 'Z':
                continue
            else:
                pr('No')
                return
    pr('Yes')


for _ in range(1):
    solve()
