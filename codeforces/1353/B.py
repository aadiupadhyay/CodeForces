for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    x=list(map(int,input().split()))
    l.sort()
    x.sort(reverse=True)
    i=0
    z=0
    j=0
    while z<k and i<n:
        if l[i]<x[j]:
            l[i]=x[j]
            i=i+1
            j=j+1
            z=z+1
        else:
            i=i+1
    print(sum(l))
            
            
