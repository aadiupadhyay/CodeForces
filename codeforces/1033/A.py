from collections import deque

def valid(x,y):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if v[x][y]:
        return False
    return True

dx=[-1,1,-1,1,1,-1,0,0]
dy=[1,-1,-1,1,0,0,-1,-1]
 
def BFS(x,y):
    q=deque()
    q.append([x,y])
    while q:
        A=q.pop()
        a,b=A[0],A[1]
        for i in range(8):
            newX,newY=a+dx[i],b+dy[i]
            if valid(newX,newY):
                v[newX][newY]=True
                q.append([newX,newY])
        





n=int(input())
Ax,Ay=map(int,input().split())
Bx,By=map(int,input().split())
Cx,Cy=map(int,input().split())
Ax-=1
Ay-=1
Bx-=1
By-=1
Cx-=1
Cy-=1

v=[[False for  i in  range(n)]for i in range(n)]


for i in range(n):
    v[Ax][i]=True
    v[i][Ay]=True
    
c=Ax
d=Ay

while c>=0 and d<n:
    v[c][d]=True
    c-=1
    d+=1
    
    

c=Ax
d=Ay

while c>=0 and d>=0:
    v[c][d]=True
    c-=1
    d-=1

c=Ax
d=Ay

while c<n and d<n:
    v[c][d]=True
    c+=1
    d+=1

c=Ax
d=Ay

while c<n and d>=0:
    v[c][d]=True
    c+=1
    d-=1

BFS(Bx,By)
print('YES' if v[Cx][Cy] else 'NO')
