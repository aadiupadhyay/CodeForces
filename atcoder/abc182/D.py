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

d=defaultdict(int)
def solve():
    n=inp()
    l=li()
    ans=0
    m=0
    s=0
    c=0
    for i in l:
        s+=i
        m=max(m,s)
        ans=max(ans,c+m)
        c+=s
    pr(ans)
            
    
solve()
