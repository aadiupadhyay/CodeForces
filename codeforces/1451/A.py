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

def solve():
    n=inp()
    ans=0
    if n==1:
        pr(0)
        return 
    if n==2:
        pr(1)
        return 
    if n==3:
        pr(2)
        return 
    if n%2:
        pr(3)
        return 
    pr(2)



        
            
    
for _ in range(inp()):
    solve()
