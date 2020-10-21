from sys  import stdin,stdout

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007

def solve():
    n=inp()
    l=li()
    ans=0
    ans+= l[0]==1
    i=1
    while i<n:
        if l[i]==0:
            i+=1
            continue
        j=i
        while j<n and l[j]==1:
            j+=1
        ans += (j-i)//3
        i=j
        
    pr(ans)
        
                
        
    
for _ in range(inp()):
    solve()
