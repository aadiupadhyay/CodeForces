def solve():

    n=int(input())

    l=list(map(int,input().split()))

    d={}

    diff=len(set(l))

    for i in l:

        d[i]=d.get(i,0)+1

    x=list(d.values())

    maxcnt=max(x)

    print(max(min(diff-1,maxcnt),min(diff,maxcnt-1)))

for _  in range(int(input())):

    solve()
