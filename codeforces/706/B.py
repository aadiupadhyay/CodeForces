import bisect as b
def solve():
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    for _ in range(int(input())):
        x=int(input())
        print(b.bisect_right(l,x))
        
solve()
