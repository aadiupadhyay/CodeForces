from sys  import stdin,stdout

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007

def solve():
    n=inp()
    s=input()
    ans='1'
    ans2='1'
    i=1
    while i<n:
        if s[i]=='1':
            ans+='1'
            ans2+='0'
            ans+='0'*(n- len(ans))
            ans2+=s[i+1:]
            print(ans)
            print(ans2)
            return
        elif s[i]=='0':
            ans+='0'
            ans2+='0'
        else:
            ans+='1'
            ans2+='1'
        i+=1
    print(ans)
    print(ans2)
    
            
        
    
for _ in range(inp()):
    solve()
