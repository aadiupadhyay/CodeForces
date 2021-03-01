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


def update(ind, x):
    while ind <= n:
        fenwick[ind] += x
        ind += ind & -ind


def sum(ind):
    s = 0
    while ind > 0:
        s += fenwick[ind]
        ind -= ind & -ind
    return s


n, q = mp()
l = [0]+li()
fenwick = [0 for i in range(n+10)]
for i in range(1, n+1):
    update(i, l[i])
for i in range(q):
    a, b, c = mp()
    if a == 0:
        b += 1
        update(b, c)
    else:
        # make 1 base index
        b += 1
        c += 1
        print(sum(c-1)-sum(b-1))
