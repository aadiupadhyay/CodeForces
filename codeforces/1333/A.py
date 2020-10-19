
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
    n,m= mp()
    for i in range(n):
        for j in range(m):
            if i==0 and j==0:
                print('W',end='')
            else:
                print('B',end='')
        print()
            

for _ in range(inp()):

    solve()

