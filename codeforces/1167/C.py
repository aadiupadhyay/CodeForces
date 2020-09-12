from sys  import stdin,stdout

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

def solve():
    n,m=mp()
    d={i:[] for i in range(1,n+1)}
    for _ in range(m):
        l=li()
        x=l[0]
        if x>1:
            for i in range(1,x):
                d[l[i]].append(l[i+1])
                d[l[i+1]].append(l[i])
 
    
                
    ans=[-1 for i in range(n+1)]
    vi=[-1 for i in range(n+1)]
    for i in range(1,n+1):
        
        if vi[i]==-1:
            
            vi[i]=i
            stack=[i]
            ans[i]=1
            while stack:
                a=stack.pop()
                for x in d[a]:
                    if vi[x]==-1:
                        ans[i]+=1
                        vi[x]=i
                        stack.append(x)
                    
 
    print(' '.join((str(ans[vi[i]]) for i in range(1,n+1))))
    
 
for _ in range(1):
    solve()
