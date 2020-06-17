def solve():
    c=0
    n=int(input())
    a=0
    i=1
    x=0
    while a+((i*(i+1))//2)<=n:
        c+=1
        a+=(i*(i+1))//2
        i+=1
    print(c)
solve()
