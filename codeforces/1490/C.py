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
    a= int(pow(n,1/3))
    b=1
    c=0
    while a>=b:
        x= a*a*a + b*b*b
        if x<n:
            b+=1
        elif x>n:
            a-=1
        else:
            c=1
            break
    
    pr('NO' if c==0 else 'YES')
for _ in range(inp()):
    solve()