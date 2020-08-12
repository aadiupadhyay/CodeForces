from sys  import stdin,stdout
 
import bisect
 
import math
 
from collections import deque
 
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
    n,m,a,b=mp()
    x=a
    y=b
    z=b
    while z<=m:
        print(x,z)
        z+=1
    z=b-1
    while z>=1:
        print(x,z)
        z-=1
    z=b

    c=1
    for i in range(1,m+1):
        if c:
            j=x+1
            while j<=n:
                print(j,i)
                j+=1
            c=0
        else:
            j=n
            while j>a:
                print(j,i)
                j-=1
            c=1
    c=1
    for i in range(m,0,-1):
        if c:
            j=x-1
            while j>=1:
                print(j,i)
                j-=1
            c=0
        else:
            j=1
            while j<x:
                print(j,i)
                j+=1
            c=1
 
    
    
 
 
 
for _ in range(1):
    solve()
