import sys,bisect

from sys  import stdin,stdout

from bisect import bisect_left,bisect_right,bisect,insort,insort_left,insort_right

from math import gcd,ceil,floor,sqrt

from collections import Counter,defaultdict,deque,OrderedDict

from queue import Queue,PriorityQueue

from string import ascii_lowercase

from heapq import *

from itertools import islice


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

def solve():
    n,m=mp()
    d={i:[] for i in range(1,n+1)}
    for _ in range(m):
        l=li()
        x=l[0]
        if x>1:
            for i in range(1,x):
                d[l[i]].append(l[i+1])
                d[l[i+1]].append(l[i])

    
                
    ans=[-1 for i in range(n+1)]
    vi=[-1 for i in range(n+1)]
    for i in range(1,n+1):
        
        if vi[i]==-1:
            
            vi[i]=i
            stack=[i]
            ans[i]=1
            while stack:
                a=stack.pop()
                for x in d[a]:
                    if vi[x]==-1:
                        ans[i]+=1
                        vi[x]=i
                        stack.append(x)
                    

    print(' '.join((str(ans[vi[i]]) for i in range(1,n+1))))
    

for _ in range(1):
    solve()
##    print("Case #{}:".format(_+1),c)
##    
