# aadiupadhyay
import os.path
from math import gcd, floor, ceil
from collections import *
import sys
sys.setrecursionlimit(4100000)
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


def DFS(node, an):
    an.append(node)
    visited[node] = 1
    for i in transpose_graph[node]:
        if not visited[i]:
            DFS(i, an)
    return an


def dfs(node):
    global order
    v[node] = 1
    for i in graph[node]:
        if not v[i]:
            dfs(i)
    order.append(node)


n, m = mp()
graph = defaultdict(list)
v = defaultdict(int)
transpose_graph = defaultdict(list)
for i in range(m):
    a, b = mp()
    graph[a].append(b)
    transpose_graph[b].append(a)
order = []
for j in range(n):
    if not v[j]:
        dfs(j)
visited = defaultdict(int)
ans = []
for i in range(n-1, -1, -1):
    if not visited[order[i]]:
        a = DFS(order[i], [])
        ans.append(a)
print(len(ans))
for i in ans:
    print(len(i), *i)
