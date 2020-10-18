from sys  import stdin,stdout

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007

def solve():
    s=st()
    pr(3)
    n=len(s)
    print('L',2)
    print('R',2)
    print('R',2*n -1 )
    
for _ in range(1):
    solve()
