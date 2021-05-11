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
    n = inp()
    deg = {chr(i): 0 for i in range(97, 97+26)}
    q = deque()
    ans = []
    l = [st() for i in range(n)]
    graph = defaultdict(list)
    for i in range(n-1):
        a, b = l[i], l[i+1]
        j = 0
        x = min(len(a), len(b))
        while j < x and a[j] == b[j]:
            j += 1
        if j < x:
            graph[a[j]].append(b[j])
            deg[b[j]] += 1
        elif j >= len(b):
            pr('Impossible')
            return
    for i in deg:
        if deg[i] == 0:
            q.append(i)
    while q:
        a = q.popleft()
        ans.append(a)
        for i in graph[a]:
            deg[i] -= 1
            if deg[i] == 0:
                q.append(i)
    if len(ans) != 26:
        pr('Impossible')
    else:
        print(''.join(ans))


for _ in range(1):
    solve()
