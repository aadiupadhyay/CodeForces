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
    n=input()
    ans=len(n)+1
    for i in range(1,1<<len(n)):
        val=0
        v=0
        for j in range(len(n)):
            if i&(1<<j):
                v+=1
                val+=int(n[j])
        if val%3==0 and ans>len(n)-v:
            ans=len(n)-v
    pr(ans if ans<len(n) else -1)
            
    
solve()
