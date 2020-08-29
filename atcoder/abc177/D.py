import sys,bisect

from sys  import stdin,stdout

from bisect import bisect_left,bisect_right,bisect,insort,insort_left,insort_right

from math import gcd,ceil,floor,sqrt

from collections import Counter,defaultdict,deque,OrderedDict

dx=[-1,1,0,0]
dy=[0,0,1,-1]


sys.setrecursionlimit(10**6)
INF = float('inf')
MOD = 998244353
mod = 10**9+7

def isPrime(n):
    if (n <= 1) :return False
    if (n <= 3) :return True
    if (n%2 == 0 or n%3 == 0):return False
    for i in range(5,ceil(sqrt(n))+1,6):
        if (n%i==0 or n%(i+2)==0):
            return False
    return True

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

def CC(d,v,i,l):
    v[i]=True
    stack=[i]
    c=1
    while stack:
        a=stack.pop()
        for i in d[a]:
            if not v[i]:
                stack.append(i)
                v[i]=True
                c+=1
    l.append(c)
    
def solve():
    n,m=mp()
    d={i:[] for i in range(1,n+1)}
    for i in range(m):
        a,b=mp()
        d[a].append(b)
        d[b].append(a)

    v=[False for i in range(n+1)]
    x=[]
    for i in range(1,n+1):
        if not v[i]:
            CC(d,v,i,x)
           
    pr(max(x))
        
        
    
for _ in range(1):
    solve()

