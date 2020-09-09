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
    l=li()
    k=[l[i+1]-l[i] for i in range(n-1)]

    ans=float('inf')
    for i in range(1,n-1):
        z=list(k)
        cur=l[i+1]-l[i-1]
        z[i-1]=cur
        ans=min(ans,max(z))
        
    pr(ans)
        

for _ in range(1):
    solve()

