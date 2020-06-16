n=int(input())
l=list(map(int,input().split()))
a,b,c=l.count(1),l.count(2),l.count(3)
z=min(a,b,c)
print(z)

if z!=0:
    while z!=0:
        x=[]
        p=[]
        for i in range(n):
            if l[i]==1:
                if 1 not in p:
                    x.append(i+1)
                    p.append(l[i])
                    l[i]=-1
            if l[i]==2:
                if 2 not in p:
                    x.append(i+1)
                    p.append(l[i])
                    l[i]=-1
            if l[i]==3:
                if 3 not in p:
                    x.append(i+1)
                    p.append(l[i])
                    l[i]=-2
        print(*x)
        z-=1
                
            
                
