
def solve():
    c=0
    n,t=map(int,input().split())
    x="1"+"0"*(n-1)
    z=int(x)
    while len(x)==n:
        if int(x)%t==0:
            print(x)
            c=1
            break
        else:
            z+=1
            x=str(z)
    if c==0:
        print("-1")
            
solve()
