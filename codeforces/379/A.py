from sys  import stdin,stdout
from collections import *
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF= float('inf')

def solve():
    a,b = mp()
    ans=a
    while a>=b:
        a-=b
        ans+=1
        a+=1
    pr(ans)
    
    

for _ in range(1):

    solve()
