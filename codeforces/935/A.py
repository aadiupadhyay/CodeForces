def solve():
    c=1
    n=int(input())
    for i in range(n//2,1,-1):
        if n%i==0:
            c+=1
    print(c)
solve()
