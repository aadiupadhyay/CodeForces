
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
    n, k = mp()
    a = list(str(n))
    for i in range(k):
        b = ''.join(sorted(a))
        c = ''.join(b[::-1])
        a = list(str(int(c)-int(b)))
    print(*a, sep='')


for _ in range(1):
    solve()
