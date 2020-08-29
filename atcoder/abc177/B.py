import sys,bisect

from sys  import stdin,stdout

from bisect import bisect_left,bisect_right,bisect,insort,insort_left,insort_right

from math import gcd,ceil,floor,sqrt

from collections import Counter,defaultdict,deque,OrderedDict

dx=[-1,1,0,0]
dy=[0,0,1,-1]


sys.setrecursionlimit(10**6)
INF = float('inf')
MOD = 998244353
mod = 10**9+7

def isPrime(n):
    if (n <= 1) :return False
    if (n <= 3) :return True
    if (n%2 == 0 or n%3 == 0):return False
    for i in range(5,ceil(sqrt(n))+1,6):
        if (n%i==0 or n%(i+2)==0):
            return False
    return True

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
    s=input()
    t=input()
    ans=float('inf')
    i=0
    while i<len(s)-len(t)+1:
        x=0
        c=0
        j=i
        
        while x<len(t):
            
            if t[x]!=s[i+x]:
                c+=1
            j+=1
            x+=1
        
        ans=min(ans,c)
        i+=1
    print(ans)
        


for _ in range(1):
    solve()

