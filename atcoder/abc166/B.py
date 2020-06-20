n,k=map(int,input().split())
l=[]
for i in range(1,k+1):
    d=int(input())
    x=list(map(int,input().split()))
    for i in x:
        if i not in l:
            l.append(i)
print(n-len(l))
