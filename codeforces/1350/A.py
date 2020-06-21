def prime(n):
    c=0
    for i in range(2,n//2+1):
        if n%i==0:
            c=1
            x=i
            break
    if c==0:
        return n
    else:
        return x
        
        
for _ in range(int(input())):

    n,k=map(int,input().split())

    if n&1:

        n+=prime(n)

        n+=2*(k-1)

    else:
        n+=2*k
    print(n)
        
