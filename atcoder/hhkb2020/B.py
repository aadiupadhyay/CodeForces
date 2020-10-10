from sys  import stdin,stdout
from math import ceil
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def valid(x,y,n,m,v,l):
    if x>=n or x<0 or y>=m or y<0:
        return False
    if v[x][y] or l[x][y]=='#':
        return False
    return True

def DFS(x,y,v,n,m,l):
    v[x][y]=True
    stack=[(x,y)]
    x=1
    while stack:
        a=stack.pop()
        A,B= a
        for i in range(4):
            newX,newY=A+dx[i],B+dy[i]
            if valid (newX,newY,n,m,v,l):
                x+=1
                stack.append((newX,newY))
                v[newX][newY]=True
    
    return x
                
                
            

def solve():
    n,m=mp()
    ans=0
    l=[st() for i in range(n)]
    for i in range(n):
        for j in range(m):
            if l[i][j]=='.':
                if j+1<m and l[i][j+1]=='.':
                    ans+=1
                if i+1<n and l[i+1][j]=='.':
                    ans+=1
    pr(ans)
                


    
for _ in range(1):
    solve()
