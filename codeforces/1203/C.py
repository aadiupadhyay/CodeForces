from sys  import stdin,stdout
from collections import *
from math import *
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007

def solve():
    n=inp()
    l=li()
    g=0
    for i in l:
        g=gcd(i,g)
    i=1
    ans=0
    while i*i<=g:
        if g%i==0:
            ans+=1
            if i!=g//i:
                ans+=1
        i+=1
    pr(ans)
    
 
    
    
for _ in range(1):
    solve()
