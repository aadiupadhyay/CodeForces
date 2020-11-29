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
    a,b,x,y=mp()

    if a==b:
        pr(x)
        return 
    if a<b:
        pr(min(x+(b-1)*y,x+2*x*(b-1)))
        return 
    pr(min((a-b-1)*y+x,2*x*(a-b-1)+x) )
for _ in range(1):
    solve()
