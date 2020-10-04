from sys  import stdin,stdout
from heapq import *
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

def solve():
    l=li()
    l.sort()
    pr(l[-1]+ l[1] -l[0])
    
for _ in range(inp()):
    solve()
