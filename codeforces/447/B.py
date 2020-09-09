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
    s=input()
    k=inp()
    ans=0
    l=li()
    for i in range(len(s)):
        ind= ord(s[i]) - 97
        
        ans+= (i+1) * l[ind]
    
    mi=float('-inf')
    for i in range(26):
        if l[i]>mi:
            mi=l[i]
            
    
    c=len(s)+1
    while k:
        
        ans+= c*mi
        c+=1
        k-=1
    pr(ans)
        
        
        

for _ in range(1):
    solve()

