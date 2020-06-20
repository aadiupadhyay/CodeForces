
def solve():
    n=int(input())
    i=1
    print(n*3+4)
    print("0 0")
    print("0 1")
    j=0
    c=1
   
    while c<=n:
        for x in range(j,j+3):
            print(i,x)
        i+=1
        j+=1
        c+=1
    print(i,j)
    print(i,j+1)

solve()
