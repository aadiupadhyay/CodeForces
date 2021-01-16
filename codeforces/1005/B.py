from sys  import stdin,stdout
 
import bisect

import math

from collections import Counter
 
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
    s=input()
    c=0
    t=input()
    i,j=len(s)-1,len(t)-1
    while i>=0 and j>=0:
        if s[i]!=t[j]:
            break
        else:
            c+=1
        i-=1
        j-=1
    if c==0:
        
        print(len(s)+len(t))
    else:
       
        print(len(s)+len(t)-2*c)
            
    
 
 
 
 
 
 
for _ in range(1):
    solve()
