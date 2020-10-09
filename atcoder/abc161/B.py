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
    n,m=mp()
    c=0
    l=li()
    x= sum(l)/(4*m)
    for i in l:
        if i>=x:
            c+=1
    pr('Yes' if c>=m else 'No')

            
for _ in range(1):

    solve()
    
    
    
                
        

