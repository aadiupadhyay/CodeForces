from sys  import stdin,stdout
from collections  import *
from math import gcd,floor,ceil
from bisect import bisect_left as bl
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

INF=float('inf')
mod=1000000007

def solve():
    a,b=mp()
    s=st()
    one=[i for i in range(len(s)) if s[i]=='1']
    if not one:
        pr(0)
        return
    first=one[0]
    last=one[-1]
    i=first
    ans=a
    prev=s[first]
    c=0
    while i<=last:
        if s[i]!=prev and s[i]=='1':
            ans+= min(a,c)
            c=0
        if s[i]=='0':
            c+=b
        prev=s[i]
        i+=1
    pr(ans)
for _ in range(inp()):
    solve()