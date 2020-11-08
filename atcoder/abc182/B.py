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
    for i in l:
        j=1
        while j*j<=i:
            if i%j==0:
                if j!=1:
                    d[j]+=1
                if j!=i//j:
                    d[i//j]+=1
            j+=1
    x=max(d.values())
    for i in d:
        if d[i]==x:
            pr(i)
            return 
    
solve()
