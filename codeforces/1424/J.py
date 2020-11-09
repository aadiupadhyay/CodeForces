import sys
from collections import deque, defaultdict, namedtuple
import heapq
from math import sqrt, factorial, gcd, ceil, atan, pi
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline()[:-1] # warning bytes
input = sys.stdin.buffer.readline # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8').strip()
import string
import operator
import random
# string.ascii_lowercase
from bisect import bisect_left, bisect_right
from functools import lru_cache, reduce
MOD = int(1e9)+7
INF = float('inf')
 
 
def solve():
    _ = int(input())
 
    MX = int(1e6) + 7
    prime = [1] * MX
    prime[0] = prime[1] = 0
    for p in range(MX):
        if prime[p]:
            for i in range(p * p, MX, p):
                prime[i] = 0
 
    ans = [0] * MX
    for i in range(1, MX):
        ans[i] = ans[i - 1] + prime[i]
        s = int(sqrt(i))
        if s * s == i:
            ans[i] -= prime[s]
 
    ns = [int(x) for x in input().strip().split()]
    sys.stdout.write("\n".join([str(ans[n] + 1) for n in ns]))
 
 
 
T = 1
# T = int(input())
for case in range(1,T+1):
    ans = solve()
 