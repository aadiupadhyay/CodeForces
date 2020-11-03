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

def solve():
    n=inp()
    l=li()
    if n<2:
        pr(-1)
        return 
    s=sum(l)
    a=0
    x=[]
    for i in range(n):
        a+=l[i]
        b=s-a
        x.append(i+1)
        if a!=b:
            if len(x)!=n:
                print(len(x))
                print(*x)
                return
    pr(-1)
    
    
    

for _ in range(1):
    solve()
