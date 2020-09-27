from sys  import stdin,stdout

#from collections import defaultdict

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

#from bisect import bisect_left,bisect_right

mod=1000000007
INF=float('inf')

def solve():
    n,k=mp()
    l=li()
    ans=[1 for i in range(n)]
    a=[]
    d={}
    dd={}
    b=[]
    for i in range(n):
        p=k-l[i]
        if p not in d:
            ans[i]=1
            d[l[i]]=1
        elif p not in dd:
            dd[l[i]]=1
            ans[i]=0
        else:
            c,cc=d[l[i]],dd[l[i]]
            if c<=cc:
                d[l[i]]+=1
                ans[i]=1
            else:
                dd[l[i]]+=1
                ans[i]=0
    print(*ans)
                
            
        
            
           
for _ in range(inp()):

    solve()
