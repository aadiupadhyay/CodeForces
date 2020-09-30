from sys  import stdin,stdout
from collections import Counter
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")
from math import ceil
mod=1000000007


'''
1
6 2
0 0 0 1 2 3
'''
def solve():
    n,k=mp()
    l=li()
    d=Counter(l)
    val=len(d)
    if k==1:
        if val!=1:
            pr(-1)
        else:
            pr(1)
        return
    if val<=k:
        pr(1)
    else:
        p=list(d.keys())
        p.sort()
        x=p[:k]
        i=0
        for j in range(n):
            if l[j]==x[i]:
                l[j]-=x[i]
            else:
                if i+1<k:
                    i+=1
                l[j]-=x[i]
        ans=1
        d=Counter(l)
        p=list(d.keys())
        p.sort()
        while p:
            x=p[:k]
            i=0
            for j in range(n):
                if l[j]==x[i]:
                    l[j]-=x[i]
                else:
                    if i+1<k:
                        i+=1
                    l[j]-=x[i]
            d=Counter(l)
            p=list(d.keys())
            p.sort()
            ans+=1
            if len(p)==1 and p==[0]:
                break

        pr(ans)
                    
            
       
                    
            
            
        
        
        

for _ in range(inp()):
    solve()
