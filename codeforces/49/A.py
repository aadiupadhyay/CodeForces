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
    s=input().lstrip().rstrip().split()
    i=len(s)-1
    while i>=0:
        x=s[i]
        for j in range(len(x)-1,-1,-1):
            if x[j].isalpha():
                p=x[j].lower()
                if p in 'aeiouy':
                    pr('YES')
                    return
                else:
                    pr('NO')
                    return
        i-=1

for _ in range(1):
    solve()
