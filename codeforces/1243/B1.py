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
    s=st()
    t=st()
    c=0
    x=[]
    for i in range(n):
        if s[i]!=t[i]:
            c+=1
            x.append(s[i])
            val= i
    if c>2:
        pr('No')
        return 
    if c==0:
        pr('Yes')
        return 
    for i in range(n):
        if t[i]==t[val] and i!=val:
            if s[val]==s[i]:
                pr('Yes')
                return 
    pr('No')

        
            
    
for _ in range(inp()):
    solve()
