from sys  import stdin,stdout
from collections  import *
from math import gcd,floor,ceil
from bisect import bisect_left
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

def solve():
    s=st()
    l=[]
    a,b,ans = 0,0,0
    for i in s:
        if i=='[':
            a+=1
        if i==']':
            if a>0:
                ans+=1
                a-=1
        if i=='(':
            b+=1
        if i==')':
            if b>0:
                ans+=1
                b-=1
    pr(ans)
        
            
for _ in range(inp()):
    solve()
