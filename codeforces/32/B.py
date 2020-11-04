from sys  import stdin,stdout
from collections  import *
from math import ceil, floor , log, gcd
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")
 
mod=1000000007
INF=float('inf')

def solve():
    s=st()
    ans=''
    i=0
    n=len(s)
    while i<n:
        if s[i]=='-':
            if s[i+1]=='.':
                ans+='1'
            else:
                ans+='2'
            i+=2
        else:
            ans+='0'
            i+=1
    if i!=n:
        ans+='0'
    pr(ans)
    

for _ in range(1):
    solve()
