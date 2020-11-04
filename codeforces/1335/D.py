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
    s=[st() for i in range(9)]
    s[0][0]=s[0][1]
    s[1][3]=s[1][4]
    s[2][6]=s[2][7]
    s[3][1]=s[3][2]
    s[4][4]=s[4][5]
    s[5][7]=s[5][8]
    s[6][2]=s[6][1]
    s[7][5]=s[7][4]
    s[8][8]=s[8][7]
    for i in s:
        print(''.join(i))
    
    
    

for _ in range(inp()):
    solve()
