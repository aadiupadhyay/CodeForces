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

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def valid(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    return l[x][y] == '.'


n, m = mp()
a, b = mp()
c, d = mp()
l = []
a, b = a-1, b-1
c, d = c-1, d-1
dist = []
now = [INF for i in range(m)]
for i in range(n):
    s = st()
    l.append(s)
    cur = list(now)
    dist.append(cur)
q = deque()
q.append((a, b))
dist[a][b] = 0
ans = -1
while q:
    x, y = q.popleft()
    if (x, y) == (c, d):
        ans = dist[x][y]
        break
    for i in range(4):
        x1, y1 = x+dx[i], y+dy[i]
        if valid(x1, y1):
            if dist[x1][y1] > dist[x][y]:
                dist[x1][y1] = dist[x][y]
                q.appendleft((x1, y1))

    for x1 in range(x-2, x+3):
        for y1 in range(y-2, y+3):
            if valid(x1, y1):
                if dist[x1][y1] > 1+dist[x][y]:
                    dist[x1][y1] = 1+dist[x][y]
                    q.append((x1, y1))


pr(ans)
