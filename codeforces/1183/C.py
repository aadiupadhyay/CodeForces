from sys  import stdin,stdout

import bisect

import math

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

def soe(limit):
    l=[1]*(limit+1)
    pp=[0]*(limit+1)
    prime=[]
    l[0]=0
    l[1]=0
    c=0
    for i in range(2,limit+1):
        if l[i]:
            for j in range(i*i,limit+1,i):
                l[j]=0
    for i in range(2,limit+1):
        if l[i]==1:
            c+=1
        if l[c]==1:
            pp[i]=1

    for i in range(1,limit+1):
        pp[i]+=pp[i-1]
    return pp

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
    k,n,a,b=mp()
    z=k//a
    if k%a==0:
        z-=1
    if z>=n:
        pr(n)
    else:
        x=k//b
        if k%b==0:
            x-=1
        if x>=n:
            c=(k-1-n*b)//(a-b)
            pr(c)
        else:
            pr(-1)
        
                

for _ in range(inp()):
    solve()
    
