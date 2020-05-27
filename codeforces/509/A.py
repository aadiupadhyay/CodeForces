n=int(input())
l=[[0]*n for i in range(n)]
ma=1
for i in range(n):
    l[0][i]=1
    l[i][0]=1
for i in range(1,n):
    for j in range(1,n):
        l[i][j]+=l[i-1][j]+l[i][j-1]
        a=l[i][j]
    if a>ma:
        ma=a
print(ma)
        
        
