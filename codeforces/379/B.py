from sys  import stdin,stdout
from collections import *
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF= float('inf')

def solve():
    n=inp()
    l=li()
    ans=''
    for i in range(n-1):
        if l[i]!=0:
            ans+= ('PRL')*(l[i]-1) + 'PR'
        else:
            ans+='R'
    if l[-1]>0:
        ans+=('PLR')*(l[-1]-1) + 'P'
    print(ans)
        
    
    

for _ in range(1):

    solve()
