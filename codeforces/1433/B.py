from sys  import stdin,stdout
from collections import *

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF= float('inf')


def solve():
    n=int(input())
    l=li()
    ans=0
    flag=0
    for i in range(n):
        if l[i]:
            flag=1
        if flag and not l[i]:
            ans+=1
    for i in range(n-1,-1,-1):
        if l[i]:
            break
        else:
            ans-=1
    pr(ans)
            
            
        
        
    
    
    
        

for _ in range(inp()):

    solve()

