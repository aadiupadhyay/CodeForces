for _ in range(int(input())):

    n=int(input())
    s=(n*(n+1))//2
    i=1
    c=0
    while i<=n:
        c+=i
        i=i<<1
    print(s-(2*c))
    
