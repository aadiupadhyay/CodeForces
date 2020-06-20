from collections import defaultdict
def solve():
    n=int(input())
    l=list(map(int,input().split()))
    o,e,r,lst=[],[],[],[]
    for i in range(len(l)):
        if l[i]&1:
            o.append(i)
        else:
            e.append(i)
    if len(o)&1:
        r.extend([o[0],e[0]])
    else:
        if len(e):
            r.extend([e[0],e[1]])
        else:
            r.extend([o[0],o[1]])

    s=defaultdict(lambda:False)

    for i in range(2*n):

        if i==r[0] or i==r[1]:
            continue
        if s[i]:
            continue
        for j in range(i+1,2*n):
            if j==r[0] or j==r[1]:
                continue
            if s[j]:
                continue
            if (l[i]&1 and l[j]&1) or (l[i]%2==0 and l[j]%2==0):
                s[i]=True
                s[j]=True

                lst.append((i+1,j+1))
                break
    for i,j in lst:
        print(i,j)

        

    
for _ in range(int(input())):

    solve()
