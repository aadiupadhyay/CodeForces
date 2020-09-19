from sys  import stdin,stdout
 
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")
 
mod=1000000007
INF=float('inf')


 
 
for _ in range(1):
    s=st()
    if s[-1]=='s':
        print(''.join(s)+'es')
    else:
        print(''.join(s)+'s')
