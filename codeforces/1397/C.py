def solve():
    

    n = int(input())
    a = list(map(int,input().split()))
    if n == 1:
        print(1,1)
        print(-a[0])
        for _ in range(2):
            print(1,1)
            print(0)
    else:
        print(1,n)
        for i in a:
            print(-i*n,end=' ')
        print('')
        print(1,n-1)
        for i in range(n-1):
            print(a[i]*(n-1),end=' ')
        print('')
        print(n,n)
        print(a[-1]*(n-1))
    
solve()