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


n, m, a, b = mp()
a -= 1
b -= 1
l = [st() for i in range(n)]
x = a+1
ans = 0

while x < n and l[x][b] == '.':
    ans += 1
    x += 1
x = a-1
while x >= 0 and l[x][b] == '.':
    ans += 1
    x -= 1
y = b+1
while y < m and l[a][y] == '.':
    ans += 1
    y += 1
y = b-1
while y >= 0 and l[a][y] == '.':
    ans += 1
    y -= 1
print(ans+1)
