
from sys import stdin, stdout
from collections import *
from math import gcd, floor, ceil
def st(): return list(stdin.readline().strip())


def li(): return list(map(int, stdin.readline().split()))
def mp(): return map(int, stdin.readline().split())
def inp(): return int(stdin.readline())
def pr(n): return stdout.write(str(n)+"\n")


mod = 1000000007
INF = float('inf')


def solve():
    n=inp()
    x=1
    y= int(n**(1/3))

    while x<=y:
        a,b = x*x*x, y*y*y
        if a+b ==n:
            pr('YES')
            return 
        elif a+b >n:
            y-=1
        else:
            x+=1
    pr('NO')

for _ in range(inp()):
    solve()
