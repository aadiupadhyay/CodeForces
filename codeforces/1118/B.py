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
    prime=[2]
    for i in range(2,limit+1):
        if l[i]:
            for j in range(i*i,limit+1,i):
                l[j]=0
    
    for i in range(3,limit+1,2):
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
    n=inp()
    l=li()
    x=[]
    o,e=0,0
    for i in range(n):
        if i&1:
            o+=l[i]
        else:
            e+=l[i]
        x.append([o,e])
    c=0
    
    for i in range(n):
        if i&1:
            a=x[i][0]-l[i]
            b=x[-1][1]-x[i][1]
            p=x[i][1]
            q=x[-1][0]-x[i][0]
            if a+b==p+q:
                c+=1
                
        else:
            a=x[i][1]-l[i]
            b=x[-1][0]-x[i][0]
            p=x[i][0]
            q=x[-1][1]-x[i][1]
            if a+b==p+q:
                c+=1
               
        
    print(c)
                
        
    



for _ in range(1):
    solve()
    
