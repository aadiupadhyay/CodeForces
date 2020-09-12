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
    l.sort()
    ans1=l[0]*l[1]*l[n-1]*l[n-2]*l[n-3]
    ans2=l[0]*l[1]*l[2]*l[3]*l[n-1]
    ans3=l[n-1]*l[n-2]*l[n-3]*l[n-4]*l[n-5]
    pr(max(ans1,ans2,ans3))
   


for _ in range(inp()):
    solve()
