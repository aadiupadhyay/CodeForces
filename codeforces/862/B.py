import sys
from sys  import stdin,stdout

import bisect

import math

mod=10**9 +7 

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

def DFS(d,visited,ver,color,value):
    value[ver]=color
    visited[ver]=True
    stack=[ver]
    while stack:
        a=stack.pop()
        for i in d[a]:
            if not visited[i]:
                visited[i]=True
                stack.append(i)
                value[i]=value[a]^1
            else:
                if value[i]==value[a]:
                    return False
    return True

def solve():
    n=inp()
    visited=[False for i in range(n+1)]
    d={i:[] for i in range(1,n+1)}
    for i in range(n-1):
        a,b=mp()
        d[a].append(b)
        d[b].append(a)

    ans=0
    value=[-1]*(n+1)
    
    for i in range(1,n+1):
        if not visited[i]:
            if not DFS(d,visited,i,0,value):
                pr(0)
                return
    a=value.count(1)
    pr(a*(n-a)-(n-1))
    
    

for _ in range(1):
    solve()
    
