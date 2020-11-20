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
    d=Counter(l)
    ele=-1
    odd=0
    v,o=[],[]
    for i in d:
        if d[i]&1:
            if n%2==0:
                pr('NO')
                return 
            else:
                odd+=1
                ele=i
                if odd>1:
                    pr('NO')
                    return 
        if d[i]%2 == 0:
            v.append(i)
            if d[i]%4==2:
                o.append(i)
    if (d[ele]-1)%2==0:
        v.append(ele)
        if (d[ele]-1)%4==2:
            o.append(ele)
    i=0
    #print(d)
    v.sort(key = lambda x:d[x],reverse=True)
    ans=[[0 for i in range(n)] for j in range(n)]
    if n&1:
        ans[n//2][n//2]=ele
        d[ele]-=1
        j,k=n//2,0
        i=0
        while k<n//2 and i<len(o):
            ans[j][k]=o[i]
            ans[j][n-1-k]=o[i]
            k+=1
            d[o[i]]-=2
            i+=1
        j,k=0,n//2
        while j<n//2 and i<len(o):
            ans[j][k]=o[i]
            ans[n-1-j][k]=o[i]
            d[o[i]]-=2
            i+=1
            j+=1
        i=0
        j,k=n//2,0
        while i<len(v) :
            while k<n//2 and d[v[i]] >0:
                if ans[j][k]==0:
                    ans[j][k]=v[i]
                    ans[j][n-1-k]=v[i]
                    d[v[i]]-=2
                k+=1
                
            i+=1
        i=0
        j,k=0,n//2
        while i<len(v):
            while j<n//2 and d[v[i]]>0:
                if ans[j][k]==0:
                    ans[j][k]=v[i]
                    ans[n-1-j][k]=v[i]
                    d[v[i]]-=2
                j+=1
                
            i+=1 
    #for i in ans:
    #    print(*i)
    #rint(d)
    x=[[d[i],i] for i in d if d[i]]
    #print(x)
    p,q=0,0
    i=0
    while i<len(x):
        a,b=x[i]
        if a%4:
            pr('NO')
            return
        if p<n//2:
            while a>0:
                ans[p][q]=b
                ans[p][n-1-q]=b
                ans[n-1-p][q]=b
                ans[n-1-p][n-1-q]=b
                a-=4
                if a>0 and a%4==0:
                    p+=1
                    if p==n//2:
                        p=0
                        q+=1
                    
            p+=1
            if p==n//2:
                p=0
                q+=1

        i+=1
    pr('YES')
    for i in ans:
        print(*i)


solve()

'''
5
3 3 4 4 5 5 5 6 6 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2
'''