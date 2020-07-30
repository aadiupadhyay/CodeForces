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
        a,b=b,a%b
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
def solve():
    n=inp()
    d={}
    for i in range(10):
        d[i]=bin(i)[2:]
    mi=float('-inf')
    for i in range(10):
        for j in range(10):
            for k in range(10):
                a=d[i]+d[j]+d[k]
                a=a[:len(a)-n]
                if a:
                    z=int(a,2)
                    if z>mi:
                        ans=str(i)+str(j)+str(k)
                        mi=z
    print(ans)
'''
                
   
def solve():
    n=inp()
    if n<=30:
        print("NO")
    else:
        c=0
        s={6,10,14}
        a=n-30
        if n==36:
            print("YES")
            print("5 6 10 15")
            return
        if n==40:
            print("YES")
            print("6 10 15 9")
            return

        if n==44:
            print("YES")
            print("6 9 14 15")
            return
            
        print("YES")
        print(6,10,14,a)
       

    
for _ in range(inp()):
    solve()
    
