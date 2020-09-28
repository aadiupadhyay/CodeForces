from sys  import stdin,stdout
from math import ceil
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007

def solve():
    n=inp()
    a=3
    c=2
    while n%a!=0:
        a+=pow(2,c)
        c+=1
    pr(n//a)
    
for _ in range(inp()):
    solve()
