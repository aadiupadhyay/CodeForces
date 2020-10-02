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
    a,b=mp()
    c=str(b)
    a+=1
    x,y=c.count('4'),c.count('7')
    while True:
        p=str(a)
        if HII(p,c):
            pr(p)
            return
        a+=1
        
    
        
        
    
    
for _ in range(1):
    solve()
