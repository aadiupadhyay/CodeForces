from sys  import stdin,stdout

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007

def solve():
    n=inp()
    ind=-1
    l=[0]
    found=0
    v=[False for i in range(n+1)]
    for i in range(1,n+1):
        x=li()
        f=0
        a=x[0]
        for j in range(a):
            if not v[x[j+1]]:
                v[x[j+1]]=True
                f=1
                break
        if not found and f==0:
            ind=i
            found=1
        l.append(x)
    if ind==-1:
        pr('OPTIMAL')
    else:

        a=l[ind]
        p=a[0]
        for i in range(1,n+1):
            if not v[i]:
                print('IMPROVE')
                print(ind,i)
                break
        
                    
                
            
            

for _ in range(inp()):
    solve()
