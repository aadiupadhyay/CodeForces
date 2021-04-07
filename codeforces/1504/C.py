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
    s = st()
    if n & 1 or s[0] != '1' or s[-1] != '1':
        pr('NO')
        return
    a = 0
    A = []
    B = []
    one = []
    zero = []
    for i in range(n):
        if s[i] == '1':
            one.append(i)
            a += 1
        else:
            zero.append(i)
        A.append(0)
        B.append(0)
    if a % 2:
        pr('NO')
        return

    for i in range(a):
        if i < a//2:
            A[one[i]] = '('
            B[one[i]] = '('
        else:
            A[one[i]] = ')'
            B[one[i]] = ')'
    b = n - a
    for i in range(b):
        if i % 2 == 0:
            A[zero[i]] = '('
            B[zero[i]] = ')'
        else:
            A[zero[i]] = ')'
            B[zero[i]] = '('
    pr('YES')
    print(*A, sep='')
    print(*B, sep='')


for _ in range(inp()):
    solve()
