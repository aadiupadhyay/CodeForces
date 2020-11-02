from sys  import stdin,stdout
from collections  import *
from math import gcd,floor,ceil
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")
INF=float('inf')

def factors(n):
    l=[]
    i=2
    while i*i<=n:
        if n%i==0:
            x=[i,0]
            while n%i==0:
                n//=i
                x[1]+=1
            l.append(x)
        i+=1
    if n>1:
        l.append([n,1])
    return l
                

def solve():
    a,b=mp()
    if a%b:
        pr(a)
        return 
    fact=factors(b)
    mi=a
    for i in fact:
        p=a
        count=0
        while p%i[0]==0:
            count+=1
            p//=i[0]
        cur=1
        while count >= i[1]:
            cur*=i[0]
            count-=1
        mi=min(mi,cur)
    pr(a//mi)
            
        
    
    
for _ in range(inp()):
    solve()
