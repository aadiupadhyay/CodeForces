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


def DFS(d,ver,visited,value,color):
    stack=[ver]
    value[ver]=color
    visited.add(ver)
    while stack:
        flag=0
        for i in d[stack[-1]]:
            if i in visited:
                if value[stack[-1]]==value[i]:
                    return False
            else:
                visited.add(i)
                flag=1
                color=value[stack[-1]]^1
                stack.append(i)
                value[i]=color
                break
        if not flag:
            stack.pop()
        
    return True
                
n=inp()
l=li()
m=inp()
k=li()
c=0
l.sort()
k.sort()
for i in range(n):
    for j in range(m):
        if abs(l[i]-k[j])<=1:
            c+=1
            k[j]=-100
            break
pr(c)
    

    
    
        
    
