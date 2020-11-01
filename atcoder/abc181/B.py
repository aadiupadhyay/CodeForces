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

n=inp()
s=0
for i in range(n):
    a,b=mp()
    a-=1
    x=a*(a+1)//2
    y=b*(b+1)//2
    s+= y-x
pr(s)

    
        
    

        
            
