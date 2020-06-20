def solve():

    n=int(input())
    if n&1:
        n+=1
    print(n//2-1)

for _  in range(int(input())):

    solve()
