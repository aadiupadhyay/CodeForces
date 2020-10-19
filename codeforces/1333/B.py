
from sys  import stdin,stdout
from collections import *
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF= float('inf')

def solve():
    n=inp()
    a=li()
    b=li()
    one,zero,ne_one= [],[],[]
    for i in range(n):
        if a[i]==0:
            zero.append(i)
        elif a[i]==-1:
            ne_one.append(i)
        else:
            one.append(i)
            
    for i in range(n-1,-1,-1):
        if a[i]==b[i]:
            continue
        if a[i]<b[i]:
            if one:
                if one[0]>=i:
                    pr('NO')
                    return
            else:
                pr('NO')
                return
        else:
            if ne_one:
                if ne_one[0]>=i:
                    pr('NO')
                    return
            else:
                pr('NO')
                return 
    pr('YES')
            
            
            

for _ in range(inp()):

    solve()

