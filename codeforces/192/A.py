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
    n=inp()
    c=0
    i=1
    while i*i<=n:
        a=(i*(i+1))//2
        b=n-a
        x=(-1+(1+8*b)**0.5)//2
        y=(-1-(1+8*b)**0.5)//2
        
        if type(x)==float and math.floor(x)==x :
            v=math.floor(x)
            if v>0 and (v*(v+1)//2)+a==n:
                c=1
                break
            
        if type(y)==float and math.floor(y)==y:
            v=math.floor(y)
            if v>0 and (v*(v+1)//2)+a==n:
                c=1
                break
            
        i+=1
        
    if c:
        print("YES")
    else:
        print("NO")
        

            


for _ in range(1):
    solve()
    
