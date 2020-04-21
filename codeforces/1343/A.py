for _ in range(int(input())):
    n=int(input())
    j=2
    x=3
    while n%x!=0:
        x=x+2**j
        j=j+1
    print(n//x)
