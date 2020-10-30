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

def BUILD(ind, ss, se):
    if ss==se:
        seg[ind]= l[ss]
        return
    mid= (ss+se) >>1
    BUILD(2*ind+1, ss,mid)
    BUILD(2*ind+2,mid+1,se)

    seg[ind]=seg[2*ind+1] + seg[2*ind+2]


def UPDATE(ind,ss,se,pos):
    if ss==se:
        seg[ind]=l[ss]
        return
    mid = (ss+se)>>1
    if mid>=pos:
        UPDATE(2*ind+1,ss,mid,pos)
    else:
        UPDATE(2*ind+2,mid+1,se,pos)
        
    seg[ind]=seg[2*ind+1] + seg[2*ind+2]
    

def QUERY(ind,ss,se,qs,qe):
    if ss> qe or se<qs:
        return 0
    if ss>=qs and se<=qe:
        return seg[ind]
    mid= (ss+se)>>1
    return  QUERY(2*ind +1 ,ss,mid,qs,qe) + QUERY(2*ind+2,mid+1,se,qs,qe)


n,q = mp()
l=li()
seg=[0 for i in range(4*n)]
BUILD(0,0,n-1)  #index , segment start , segment end
for i in range(q):
    a,b,c= mp()
    if a==0:
        l[b]+=c
        UPDATE(0,0,n-1,b)
    else:
        print(QUERY(0,0,n-1,b,c-1))
