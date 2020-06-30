from sys  import stdin,stdout

import bisect

import math

def st():
    return list(stdin.readline())

def inp():
    return int(stdin.readline())

def li():
    return list(map(int,stdin.readline().split()))

def mp():
    return map(int,stdin.readline().split())

def pr(n):
    stdout.write(str(n)+"\n")

def soe(limit):
    l=[1]*(limit+1)
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

def power(a,n):
    r=1
    while n:
        if n&1:
            r=(r*a)
            n=n-1
        else:
            a=(a*a)
            n=n>>1
    return r
    
def solve():
    n,m=mp()
    x=[]
    p=[]
    for i in range(m):
        s=input().split()
        x.append(s)
        if len(s[0])<=len(s[1]):
            p.append(s[0])
        else:
            p.append(s[1])
    l=input().split()
    y=[]
    for i in l:
        if i in p:
            y.append(i)
        else:
            for j in range(m):
                if i in x[j]:
                    if len(x[j][0])<=len(x[j][1]):
                        y.append(x[j][0])
                    else:
                        y.append(x[j][1])
    print(*y)
    


solve()
##
##for _ in range(inp()):
##    solve()
    
