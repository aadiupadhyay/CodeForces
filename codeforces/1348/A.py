for _ in range(int(input())):
    n=int(input())
    l=[2**i for i in range(1,n+1)]
    s=l[-1]
    s+=sum(l[:n//2-1])
    a=sum(l[n//2-1:-1])
    print(abs(s-a))
            