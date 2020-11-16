from sys  import stdin,stdout
from collections  import *
from math import gcd,floor,ceil
from bisect import bisect_left as bl
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')
ANS=[]

def solve():
    s=st()
    n=len(s)
    s=s[::-1]
    ans=''
    i=0
    p=set()
    while i<n:
        c=1
        x=s[i]
        i+=1
        while i<n and s[i]==x:
            i+=1
            c+=1
        if c%2:
            p.add(x)
    for i in range(97,97+26):
        if chr(i) in p:
            print(chr(i),end='')
    print()
            
            
        
            
        
 
     
for _ in range(inp()):
    solve()

