# aadiupadhyay
import os.path
# testing extension
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


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
n, m, k = mp()
l = []
now = [INF for i in range(m)]
distance = []
for i in range(n):
    cur = list(now)
    s = st()
    l.append(s)
    distance.append(cur)
a, b, c, d = mp()
a, b, c, d = a-1, b-1, c-1, d-1
q = deque()
q.append((a, b))
distance[a][b] = 0
ans = -1
while q:
    x, y = q.popleft()
    if (x, y) == (c, d):
        ans = distance[x][y]
        break
    for i in range(4):
        for j in range(1, k+1):
            x1, x2 = x+j*dx[i], y+j*dy[i]
            if x1 < 0 or x2 < 0 or x1 >= n or x2 >= m or l[x1][x2] == '#' or distance[x1][x2] < 1+distance[x][y]:
                break
            else:
                if distance[x1][x2] > 1 + distance[x][y]:
                    distance[x1][x2] = 1+distance[x][y]
                    q.append((x1, x2))
pr(ans)
