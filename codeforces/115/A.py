import sys
from sys  import stdin,stdout

import bisect

import math
sys.setrecursionlimit(10000000)
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
'''
def DFS(d,ver,visited,value):
    
    visited[ver]=True
    size=1
    for i in d[ver]:
        if not visited[i]:
            size+=DFS(d,i,visited,value)
        value[ver]=size
        return size
'''

def dfs(node, level, mydict, visited):
    visited[node] = True
    maxi = level
    for child in mydict[node]:
        if not visited[child]:
            maxi = max(maxi, dfs(child, level + 1, mydict, visited))
    return maxi
 
def solve():
 
    n = int(input())
    mydict = {i : [] for i in range(1, n+1)}
    parent = {i : -1 for i in range(1, n+1)}
    for i in range(n):
        child = int(input())
        if child != -1:
            mydict[child].append(i+1)
            parent[i+1] = child
    # print(mydict)
 
    visited = [False]*(n+1)
    max_level = 0
    for i in range(1, n+1):
        if not visited[i] and parent[i]==-1 :
            max_level = max(max_level, dfs(i, 0, mydict, visited))
 
    print(max_level + 1)
    

    

for _ in range(1):
    solve()
    
