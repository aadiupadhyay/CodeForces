from sys  import stdin,stdout
from collections  import *

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

ma= 10**3 +1 
fact=[0 for i in range(ma)]
invfact=[0 for i in range(ma)]
fact[0]=1
for i in range(1,ma):
    fact[i]= (i%mod *fact[i-1]%mod)%mod

invfact[ma-1]= pow(fact[ma-1],mod-2,mod)
for i in range(ma-2,-1,-1):
    invfact[i]= (invfact[i+1]%mod *(i+1) %mod)%mod

def ncr(n,r):
    if (r>n or n<0 or r<0):
        return 0
    return ((fact[n]%mod *invfact[r]%mod)%mod *(invfact[n-r]%mod)%mod )%mod


def solve():
    n,x,p = mp()
    l,r=0,n
    s,b=0,0
    while l<r:
        m= (l+r)//2
        if m<p:
            s+=1
            l=m+1
        elif m>p:
            b+=1
            r=m
        else:
            l=m+1
    ans=1
    ans= (ans%mod * ncr(x-1,s)%mod)%mod
    ans= (ans%mod * ncr(n-x,b)%mod)%mod
    ans= (ans%mod * fact[s]%mod)%mod
    ans= (ans%mod * fact[b]%mod)%mod
    ans= (ans%mod * fact[n-s-b-1]%mod)%mod
    pr(ans)
        
    
    
for _ in range(1):
    solve()
