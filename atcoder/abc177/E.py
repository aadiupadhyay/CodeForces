from sys  import stdin,stdout
from collections  import *
from math import ceil, floor , log, gcd
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")
 
mod=1000000007
INF=float('inf')

maxN=10**6 + 10
l=[i for i in range(maxN+10)]
prime=[]
for i in range(2,maxN):
    if l[i]==i:
        prime.append(i)
    for  j in range(len(prime)):
        if prime[j]>l[i] or i*prime[j]>maxN:
            break
        l[i*prime[j]]=prime[j]

 
def solve():
    n=inp()
    k=li()
    g=0
    for i in range(n):
        g=gcd(g,k[i])
        if g==1:
            break
    if g!=1:
        pr('not coprime')
        return
    d={}
    for i in range(n):
        x=k[i]
        p=set()
        val=0
        while x!=1:
            p.add(l[x])
            x=x//l[x]
        for i in p:
          if i not in d:
            d[i]=1
          else:
            pr('setwise coprime')
            return 
    pr('pairwise coprime')
 
for _ in range(1):
    solve()
