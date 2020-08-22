import sys,bisect

from sys  import stdin,stdout

from bisect import bisect_left,bisect_right,bisect,insort,insort_left,insort_right

from math import gcd,ceil,floor,sqrt

from collections import Counter,defaultdict,deque,OrderedDict

from queue import Queue,PriorityQueue

from string import ascii_lowercase

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
    
def solve():
    r,c,m=mp()
    row={}
    col={}
    dd={}
    d={}
    for i in range(m):
        l=li()
        a=l[0]
        b=l[1]
        row[a]=row.get(a,0)+1
        col[b]=col.get(b,0)+1
    
        if a in d:
            d[a].add(b)
        else:
            d[a]={b}

        if b in dd:
            dd[b].add(a)
        else:
            dd[b]={a}
    
    miR,miC=float('-inf'),float('-inf')
    
    for i in row:
        if row[i]>miR:
            miR=row[i]
            R=i
    for i in col:
        if col[i]>miC:
            miC=col[i]
            C=i

    ans=float('-inf')

    for i in col:
        c=miR+col[i]
        if i in d[R]:
            c-=1
        ans=max(ans,c)

    for  i in row:
        c=miC+row[i]
        if i in dd[C]:
            c-=1
        ans=max(ans,c)

    pr(ans)
        
        
        
            

for _ in range(1):
    solve()
    
