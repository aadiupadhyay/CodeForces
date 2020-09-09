import sys,bisect

from sys  import stdin,stdout

from bisect import bisect_left,bisect_right,bisect,insort,insort_left,insort_right

from math import gcd,ceil,floor,sqrt

from collections import Counter,defaultdict,deque,OrderedDict

sys.setrecursionlimit(10**6)
INF = float('inf')
MOD = 998244353
mod = 10**9+7

def st():
    return list(stdin.readline().strip())

def inp():
    return int(stdin.readline())

def li():
    return list(map(int,stdin.readline().split()))

def mp():
    return map(int,stdin.readline().split())

def pr(n):
    stdout.write(str(n)+"\n")
    
def solve():
    n=inp()
    if n&1:
        pr(-1)
        return
    l=[i for i  in range(n+1)]
    x=n
    for  i in range(1,n//2 +1):
        l[i]=x
        l[l[i]]=i
        x-=1
    print(*l[1:])
        
        
        
        
        

for _ in range(1):
    solve()

