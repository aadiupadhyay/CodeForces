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
    
def DFS(dictionary,vertex,visited):
    visited[vertex]=True
    stack=[vertex]
    print(vertex)
    while stack:
        a=stack.pop()
        for i in dictionary[a]:
            if not visited[i]:
                print(i)
                visited[i]=True
                stack.append(i)


def BFS(dictionary, vertex,visited):
    visited[vertex]=True
    q=deque()
    q.append(vertex)
    while q:
        a=q.popleft()
        for i in dictionary[a]:
            if not visited[i]:
                visited[i]=True
                q.append(i)
                print(i)

                


def soe(limit):
    l=[1]*(limit+1)
    l[0]=0
    l[1]=0
    prime=[]
    for i in range(2,limit+1):
        if l[i]:
            for j in range(i*i,limit+1,i):
                l[j]=0
    
    for i in range(2,limit+1):
        if l[i]:
            prime.append(i)
    return prime

def segsoe(low,high):
    limit=int(high**0.5)+1
    prime=soe(limit)
    n=high-low+1
    l=[0]*(n+1)
    for i in range(len(prime)):
        lowlimit=(low//prime[i])*prime[i]
        if lowlimit<low:
            lowlimit+=prime[i]
        if lowlimit==prime[i]:
            lowlimit+=prime[i]
        for j in range(lowlimit,high+1,prime[i]):
            l[j-low]=1
    for i in range(low,high+1):
        if not l[i-low]:
            if i!=1:
                print(i)
                
def gcd(a,b):
    while b:
        a=a%b
        b,a=a,b
    return a

def power(a,n):
    r=1
    while n:
        if n&1:
            r=(r*a)
        a*=a
        n=n>>1
    return r

def don(d,ans,vi,i):
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
