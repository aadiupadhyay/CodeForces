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
    l=[0]+li()
    for i in range(1,n+1):
        y=i
        x=l[i]
        z=l[x]

        if l[z]==i:
    
            pr('YES')
            return
    pr('NO')
        
    
        
            
    
    

for _ in range(1):
    solve()
