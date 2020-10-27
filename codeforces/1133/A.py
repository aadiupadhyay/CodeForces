from sys  import stdin,stdout
from collections  import *
from math import ceil, floor , log
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")
 
mod=1000000007
INF=float('inf')
 
def solve():
    s=input().split(':')
    t=input().split(':')

    t1 = int(s[0])*60 + int(s[1])
    t2 = int(t[0])*60 + int(t[1])
    t3 = (t1+t2)>>1
    H, M = t3//60 , t3%60
    print(str(H).zfill(2)+':'+str(M).zfill(2))
    
    
 
 
 
for _ in range(1):
    solve()
