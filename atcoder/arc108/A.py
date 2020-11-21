from sys  import stdin,stdout
from collections  import *
from math import gcd,floor,ceil
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

def solve():

    n,m=mp()
    i=1
    while i*i<=m:
        if m%i==0:
            if i+(m//i) ==n:
                pr('Yes')
                return 
        i+=1
    pr('No')
solve()