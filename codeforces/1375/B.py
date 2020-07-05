from sys  import stdin,stdout

import bisect

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
    n,m=mp()
    l=[]
    for i in range(n):
        a=li()
        l.append(a)
    counter=0
    for i in range(n):
        
        for j in range(m):
            x=4
            if i==0 or i==n-1:
                x-=1
            if j==0 or j==m-1:
                x-=1

            if x<l[i][j]:
                print("NO")
                return
          
            l[i][j]=x
    print("YES")
    for i in l:
        print(*i)
                






for _ in range(inp()):
    solve()
    
