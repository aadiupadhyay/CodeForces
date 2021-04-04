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
    l = li()
    odd = []
    even = []
    l.sort()
    f, s = 0, 0
    for i in l:
        if i & 1:
            odd.append(i)
        else:
            even.append(i)
    turn = 1
    while odd and even:
        if turn:
            if even[-1] > odd[-1]:
                f += even[-1]
                even.pop()
            else:
                odd.pop()
        else:
            if odd[-1] > even[-1]:
                s += odd[-1]
                odd.pop()
            else:
                even.pop()
        turn ^= 1
    while even:
        if turn:
            f += even[-1]
        turn ^= 1
        even.pop()
    while odd:
        if not turn:
            s += odd[-1]
        turn ^= 1
        odd.pop()
    if f == s:
        pr('Tie')
    elif f > s:
        pr('Alice')
    else:
        pr('Bob')


for _ in range(inp()):
    solve()
