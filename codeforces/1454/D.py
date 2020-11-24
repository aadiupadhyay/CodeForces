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
    n=inp()
    p=n
    i=2
    d={}
    if n%i==0:
        d[2]=0
        while n%2==0:
            d[2]+=1
            n//=2
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            d[i]=0
            while n%i==0:
                d[i]+=1
                n=n//i
    if n>1:
        d[n]=1
    x=[[d[i],i] for i in d]
    x.sort(reverse=True)
    a=x[0][1]
    b=x[0][0]
    print(b)
    print((str(a)+' ')*(b-1),end='')
    pro=a
    for i in d:
        if i==a:
            continue
        pro*=pow(i,d[i])
    pr(pro)

    
    
for _ in range(inp()):
    solve()
