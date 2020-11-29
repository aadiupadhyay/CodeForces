from sys  import stdin,stdout
from collections  import *
from math import gcd,floor,ceil
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

def solve():
    n=inp()
    l=li()
    even=[]
    odd=[]
    for i in range(len(l)):
        if l[i]%2:
            odd.append(i+1)
        else:
            even.append(i+1)
    if even and odd:
        if len(even)%2==0 and len(odd)%2==0:
            even.pop()
            even.pop()
        else:
            even.pop()
            odd.pop()

    elif even:
        even.pop()
        even.pop()
    else:
        odd.pop()
        odd.pop()
    #print(even,odd)
    for i in range(0,len(even)-1,2):
        print(even[i],even[i+1])
    for i in range(0,len(odd)-1,2):
        print(odd[i],odd[i+1])
    #print()

        
            
    
for _ in range(inp()):
    solve()
