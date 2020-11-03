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

def update(ind,val,n):
    while ind <= n:
        BIT[ind]+=val
        ind+= ind&(-ind)
        
def su(ind,n):
    s=0
    while ind>0:
        s+=BIT[ind]
        ind-= ind&(-ind)
    return s
        
    

n,q=mp()
l=['x']+li()
BIT=[0 for i in range(n+20)]
for i in range(1,n+1):
    update(i,l[i],n)
ans=[]
for i in range(q):
    a,b,c=mp()
    if a==0:
        update(b+1,c,n)
    else:
        ans.append(su(c,n)-su(b,n))
print('\n'.join(map(str,ans)))
