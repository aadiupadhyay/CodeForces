def solve():
    l=list(map(int,input().split()))
    k=[]
    c=0
    for i in l:
        if i not in k:
            k.append(i)
        else:
            c+=1
    print(c)
solve()
