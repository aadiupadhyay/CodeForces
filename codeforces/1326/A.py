
def solve():
    n=int(input())
    if n==1:
        print("-1")
    else:
        if (n-1)%3:
            print("2"*(n-1)+"3")
        else:
            print("2"*(n-2)+"33")
for i in range(int(input())):
    solve()
