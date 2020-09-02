n,m=map(int,input().split())
row=set()
col=set()
ans=0
for  i in range(n):
    s=input()
    for j in range(m):
        if s[j]=='S':
            row.add(i)
            col.add(j)
ans=n*m
x=len(row)*len(col)

print(ans-x)
    
