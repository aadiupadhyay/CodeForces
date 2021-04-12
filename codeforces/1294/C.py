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

    def factor(n, x):

        if isprime(n):
            return False
        i = 2
        while i*i <= n:
            if n % i == 0:
                if i != n//i:
                    if i != x and n//i != x:
                        print('YES')
                        print(i, n//i, x)
                        return True
            i += 1
        return False

    def isprime(n):
        if n <= 4:
            return n == 2 or n == 3
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(n**0.5)+1, 6):
            if n % i == 0 or n % (i+2) == 0:
                return False
        return True
    n = inp()
    if n == 1 or isprime(n):
        pr('NO')
        return
    i = 2
    while i*i <= n:
        if n % i == 0:
            if n//i != i:
                a, b = n//i, i
                if factor(a, b):
                    return
                if factor(b, a):
                    return
        i += 1
    pr('NO')


for _ in range(inp()):
    solve()
