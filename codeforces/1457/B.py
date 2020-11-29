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
    n,k=mp()
    l=li()
    ma=INF 
    for x in range(1,101):
        a=0
        y=0
        while y<n:
            if l[y]!=x:
                a+=1
                y+=k-1
            y+=1
        ma=min(ma,a)
    pr(ma)


        
            
    
for _ in range(inp()):
    solve()
