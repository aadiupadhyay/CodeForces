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
    def BFS(node):
        nonlocal unseen
        q = deque()
        q.append(node)
        v[node] = 1
        unseen.discard(node)
        future = set()
        res = 0
        while q:
            res += 1
            a = q.popleft()
            for i in graph[a]:
                if v[i]:
                    continue
                if i in unseen:
                    future.add(i)
                    unseen.discard(i)
            for i in unseen:
                v[i] = 1
                q.append(i)
            unseen = set(future)
            future = set()
        return res

    n, m = mp()
    graph = defaultdict(list)
    for i in range(m):
        a, b = mp()
        graph[a].append(b)
        graph[b].append(a)
    v = defaultdict(int)
    ans = []
    unseen = set(range(1, n+1))
    for i in range(1, n+1):
        if not v[i]:
            cur = BFS(i)
            ans.append(cur)
    print(len(ans))
    print(*sorted(ans))


for _ in range(1):
    solve()
