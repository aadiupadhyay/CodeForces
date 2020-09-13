from sys  import stdin,stdout

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007

def solve():
    a,b,c,d=mp()
    x=a*d
    y=a*c
    z=b*d
    p=b*c
    pr(max(x,y,z,p))
    


for _ in range(1):
    solve()
