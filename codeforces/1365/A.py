def solve():
    a,b=map(int,input().split())
    x=[[0]*b for i in range(a)]
    l=[]
    k=[]
    for i in range(a):
        s=list(map(int,input().split()))
        for j in range(b):
            if s[j]==1:
                l.append(i)
                k.append(j)
            x[i][j]=s[j]
    p,q=set(l),set(k) 
    z=[i for i in range(a)]
    v=[i for i in range(b)]
    z,v=set(z),set(v)
    z=z-p
    v=v-q
    h=min(len(z),len(v))
    if h&1:
        print("Ashish")
    else:
        print("Vivek")
    
           
        

for _ in range(int(input())):
    solve()
    
