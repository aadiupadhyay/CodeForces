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
    l=li()
    d=defaultdict(list)
    for i in range(n):
        d[l[i]].append(i+1)
    ma= INF
    for i in d:
        if len(d[i])<ma:
            ma=len(d[i])
            val=i
            index= d[i][0]
    ans=[]
    for i in d:
        if i!=val:
            for j in d[i]:
                ans.append((index,j))
    u=len(d[val])
   
    cur= n-u
   
    
    if cur <u-1:
        print('NO')
        return
    i=1
    while i<u:
        for j in d:
            if j!=val:
                for k in d[j]:
                    ans.append((d[val][i],k))

                    i+=1
                    if i>=u:
                        print('YES')
                        for p in ans:
                            print(*p)
                        return
    print('YES')
    for p in ans:
        print(*p)
        
    
            
            
        
        
        
    
    
    
        

for _ in range(inp()):

    solve()

