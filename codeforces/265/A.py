from sys  import stdin,stdout

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF= float('inf')
def solve():
    s=st()
    t=st()
    i=0
    j=0
    while j<len(t):
        i+=(t[j]==s[i])
        j+=1
    pr(i+1)
  
for _ in range(1):
    solve()
