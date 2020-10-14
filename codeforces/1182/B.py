from sys  import stdin,stdout

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007

def solve():
    n,m=mp()
    mat=[st() for i in range(n)]
    star=0
    for  i in range(n):
        for j in range(m):
            if mat[i][j]=='*':
                star+=1
    if star==0 or star>=m+n:
        pr('NO')
        return 
    for i in range(n):
        for j in range(m):
            if mat[i][j]=='*':
                c=-1
                p=i
                flag=False
                while p>=0 and mat[p][j]=='*':
                    p-=1
                    flag=True
                    c+=1
                p=i+1
                if not flag:
                    continue
                flag=False
                while p<n and mat[p][j]=='*':
                    p+=1
                    c+=1
                    flag=True
                if not flag:
                    continue
                flag=False
                p=j
                while p>=0 and mat[i][p]=='*':
                    p-=1
                    c+=1
                    flag=True
                if not flag:
                    continue
                
                p=j+1
                flag=False
                while p<m and mat[i][p]=='*':
                    p+=1
                    flag=True
                    
                    c+=1
                if not flag:
                    continue
                if c==star:
                    #print(i,j)
                    pr('YES')
                    return
    pr('NO')
                
    


    
    
for _ in range(1):
    solve()
