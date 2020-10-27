from sys  import stdin,stdout
from collections  import *
from math import *
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

def solve():

    n=inp()
    a,b =mp()
    if a%n==0 or b%n==0:
        pr('OK')
        return 
    pr('OK' if a//n != b//n else 'NG')

for _ in range(1):
    solve()

