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


def update(index, delta):
    while index <= n:
        BIT[index] += delta
        index += index & -index


def value(index):
    c = 0
    while index > 0:
        c += BIT[index]
        index -= index & -index
    return c


n, q = mp()
l = [0] + li()
query = []
ans = []
BIT = [0 for i in range(n+10)]
total = 0
last = defaultdict(int)
k = 0
for i in range(q):
    start, end = mp()
    query.append([start, end, i])
    ans.append(0)

query.sort(key=lambda x: x[1])

for i in range(1, n+1):
    if last[l[i]] != 0:
        update(last[l[i]], -1)
    else:
        total += 1
    update(i, 1)
    while k < q and query[k][1] == i:
        ans[query[k][2]] = total - value(query[k][0]-1)
        k += 1
    last[l[i]] = i
print(*ans, sep='\n')
