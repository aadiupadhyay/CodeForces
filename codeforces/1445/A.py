from sys  import stdin,stdout
from collections  import *
from math import gcd,floor,ceil
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

t=inp()
for _ in range(t):
    n,x=mp()
    l=li()
    f=0
    k=li()
    if _!=t-1:
        s=input()
    l.sort()
    k.sort(reverse=True)
    for i in range(n):
        p=l[i]+k[i]
        if p>x:

            f=1
            break
    if f==0:
        pr('Yes')
    else:
        pr('No')
    

        
            
