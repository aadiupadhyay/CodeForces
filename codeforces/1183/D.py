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
    n=inp()
    x=[]
    l=li()
    d={}
    for i in l:
        d[i]=d.get(i,0)+1
    for i in d:
        x.append(d[i])
    x.sort(reverse=True)
    s=set()
    c=0
    for i in x:
        if i not in s:
            c+=i
            s.add(i)
        else:
            while i in s:
                i-=1
            if i>0:
                s.add(i)
                c+=i
            
    print(c)


    
            
                

for _ in range(inp()):
    solve()
    
