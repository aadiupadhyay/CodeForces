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

n, m = mp()
d = defaultdict(list)
for _ in range(m):
    a, b, c = mp()
    d[(a, c)].append(b)
    d[(b, c)].append(a)
Q = inp()
v = [0 for i in range(n+1)]
for i in range(Q):
    x, y = mp()
    ans = 0
    for j in range(1, m+1):
        q = deque()
        q.append((x, j))
        copy_visited = list(v)
        copy_visited[x] = 1
        while q:
            a, b = q.popleft()
            if a == y:
                ans += 1
                break
            for k in d[(a, b)]:
                if not copy_visited[k]:
                    copy_visited[k] = 1
                    q.append((k, b))
    print(ans)
