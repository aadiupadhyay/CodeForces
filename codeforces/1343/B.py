for _ in range(int(input())):
    n=int(input())
    l=[]
    if n%4!=0:
        print("NO")
    else:
        for i in range(n//2):
            l.append(2*(i+1))
        x=sum(l)
        z=n//2
        j=1
        s=0
        k=[]
        while s<x:
            a=(2*j)-1
            s=s+a
            j=j+1
            k.append(a)
        print("YES")
        q=sum(k)-x
        k.remove(q)
        l=l+k
        print(*l)
            
            
