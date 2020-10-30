

from sys  import stdin,stdout
from collections  import *
from math import factorial
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

dx=[-1,1,0,0]
dy=[0,0,1,-1]
 
def solve():
    n=inp()
    i=1
    ans=0
    while i*i<=n:
        if n%i==0:
            ans+=1
            if i!= n//i:
                ans+=1
        i+=1
    pr(ans)

for _ in range(1):
    solve()
