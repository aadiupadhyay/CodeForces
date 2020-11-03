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
    s=st()
    i=0
    j=len(s)-1
    n=len(s)
    c=0
    while i<=j:
        c+= s[i]!=s[j]
        i+=1
        j-=1
    if c==1:
        pr('YES')
    else:
        if c==0:
            if n&1:
                pr('YES')
            else:
                pr('NO')
        else:
            pr('NO')
    
    
    

for _ in range(1):
    solve()
