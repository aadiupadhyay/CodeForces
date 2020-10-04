from sys  import stdin,stdout
from math import gcd
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

def solve():
    n,k=mp()
    l=[0,1]
    if k&1:
        print(1)
        return
    
    a=1
    for i in range(2,55):
        X=pow(2,a)
        a+=1
        Y=pow(2,a)
        if (k-X)%(Y)==0:
            print(i)
            return

    
    
        
        
            
                
            
            

for _ in range(1):
    solve()
