from sys  import stdin,stdout
from math import gcd
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

def HII(p,c):
    x=''
    j=0
    for i in range(len(p)):
        if p[i]=='4':
            if j<len(c) and c[j]!='4':
                return False
            
            x+=p[i]
            j+=1
        elif p[i]=='7':
            if j<len(c) and c[j]!='7':
                return False
            j+=1
            x+=p[i]
            
    return x==c

def solve():
    n=inp()
    s=st()
    s.sort()
    pr(''.join(s))
    
        
        
    
    
for _ in range(1):
    solve()
