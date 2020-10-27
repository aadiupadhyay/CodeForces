from sys  import stdin,stdout
from collections  import *
from math import *
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

def solve():

    n=inp()
    x=100
    ans=0
    while x<n:
        x+= x//100
        ans+=1
    pr(ans)

for _ in range(1):
    solve()

