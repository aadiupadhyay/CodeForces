from sys  import stdin,stdout
from collections import deque
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')



def solve():
    x,y,z=mp()
    x,y=y,x
    x,z=z,x
    print(x,y,z)
    

            
for _ in range(1):

    solve()
    
    
    
                
        

