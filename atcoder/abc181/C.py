from sys  import stdin,stdout
from collections  import *
from math import gcd,floor,ceil
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

def colinear(x1,y1,x2,y2,x3,y3):
    return (y1-y2)*(x1-x3) == (y1-y3)*(x1-x2)
n=inp()
b=2
l=[li() for i in range(n)]
for i in range(n):
    for j in range(i+1,n):
        c=2
        for k in range(n):
            if i==k or k==j:
                continue
            if colinear(l[i][0],l[i][1],l[j][0],l[j][1],l[k][0],l[k][1]):
                c+=1
        b=max(b,c)
pr('Yes' if b>=3 else 'No')
    
