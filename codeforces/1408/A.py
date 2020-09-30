from sys  import stdin,stdout

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007

def solve():
    n=inp()
    a=li()
    b=li()
    c=li()
    pre=-1
    ans=[]
    for i in range(n):
        x=[a[i],b[i],c[i]]
        for j in x:
            if j!=pre:
                ans.append(j)
                pre=j
                break
    
    if ans[0]==ans[-1]:
        p=ans[-2]
        x=[a[-1],b[-1],c[-1]]
        for i in x:
            if i!=ans[0] and i!=p:
                ans[-1]=i
                break
    print(*ans)
       
    


for _ in range(inp()):
    solve()
