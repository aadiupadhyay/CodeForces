from sys  import stdin,stdout

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

def solve():
    n,k=mp()
    l=li()
    o,e=0,0
    for i in l:
        o+=i%2
        e+=i%2==0
    if o==0:
        pr('No')
        return
    
    if k%2==0:
        
        for i in range(1,e+1,2):
            if k-i <=o:
                pr('Yes')
                return
        pr('No')
    else:
        for i in range(0,e+1,2):
            if k-i <=o:
                pr('Yes')
                return
        pr('No')
    
            



for _ in range(inp()):

    solve()
