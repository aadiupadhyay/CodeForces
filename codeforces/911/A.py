from sys  import stdin,stdout
from math import floor
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
'''
prime=[]
i=2
l=[True for i in range(10**5+1)]
while i*i <= 10**5 :
    if l[i]:
        for j in range(i*i,10**5+1,i):
            l[j]=False
    i+=1
for i in range(2,10**5+1):
    if l[i]:
        prime.append(i)
'''

def solve():
    n=inp()
    l=li()
    a=min(l)
    x=[]
    for i in range(n):
        if l[i]==a:
            x.append(i)
    
    mi=float('inf')
    for i in range(1,len(x)):
        mi=min(mi,x[i]-x[i-1])
    pr(mi)
            
    
    
for _ in range(1):
    solve()

