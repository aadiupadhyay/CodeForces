# aadiupadhyay
import sys
from collections import *
import os.path
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
    n, q, k = mp()
    l = li()
    A = []
    for i in range(q):
        a, b = mp()
        size = b-a+1
        ans = l[b-1] - l[a-1] + k - 2*size + 1
        A.append(ans)
    print(*A, sep='\n')


solve()
