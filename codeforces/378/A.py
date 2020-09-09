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
    a,b=mp()
    l=[0,0,0]
    for i in range(1,7):
        x=abs(a-i)
        y=abs(b-i)
        if x==y:
            l[1]+=1
        elif x<y:
            l[0]+=1
        else:
            l[2]+=1
    print(*l)
        
        


for _ in range(1):
    solve()

