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
    x=sum(map(int,s))
    c,d=0,0
    for i in s:
        if int(i)%2==0:
            c+=1
        if i=='0':
            d+=1
    if x%3==0 and c>=2 and d>=1:
        pr('red')
    else:
        pr('cyan')
            
        
 
     
for _ in range(inp()):
    solve()

