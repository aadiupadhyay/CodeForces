from sys  import stdin,stdout
from math import *
from collections import *
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007

def solve():
    n=inp()
    l=[]
    i=1
    while i*i<=n:
        if n%i==0:
            l.append(i)
            if n//i != i:
                l.append(n//i)
        i+=1
    print('\n'.join(str(i) for i in sorted(l)))
    
for _ in range(1):
    solve()
