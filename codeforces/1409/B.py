import sys,bisect

from sys  import stdin,stdout

from bisect import bisect_left,bisect_right,bisect,insort,insort_left,insort_right

from math import gcd,ceil,floor,sqrt

from collections import Counter,defaultdict,deque,OrderedDict

from queue import Queue,PriorityQueue

from string import ascii_lowercase


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
  
def solve():
    a,b,x,y,n=mp()
    X=a-x
    Y=b-y
    cp=n
    XX=a
    YY=b
    Z=max(X,Y)
    if Z==X:
    
        c=min(n,X)
        n-=c
        a-=c
        d=min(n,Y)
        n-=d
        b-=d

        c=min(cp,YY-y)
        cp-=c
        YY-=c

        d=min(cp,XX-x)
        cp-=d
        XX-=d
        
        print(min(a*b, XX*YY))
    else:
        
        c=min(n,Y)
        n-=c
        b-=c
        d=min(n,X)
        n-=d
        a-=d

        c=min(cp,XX-x)
        cp-=c
        XX-=c

        d=min(cp,YY-y)
        cp-=d
        YY-=d
        
        print(min(a*b,XX*YY))



for _ in range(inp()):
    solve()
