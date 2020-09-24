from sys  import stdin,stdout

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF= float('inf')
def solve():
    n,m=mp()
    mat = []
    for i in range(n):
        mat.append(list(input()))
     
    maximum = []
    for i in range(m):
        maxi = -INF 
        for j in range(n):
            maxi = max(maxi, int(mat[j][i]))
        maximum.append(maxi)
    
    suc = 0
    for i in range(n):
        flag = 0
        for j in range(m):
            if int(mat[i][j])==maximum[j]:
                flag = 1
                break
        if flag==1:
            suc+=1
    print(suc)
for _ in range(1):
    solve()
