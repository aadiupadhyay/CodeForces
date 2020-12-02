# Aaditya Upadhyay 
# ..............
# ╭━┳━╭━╭━╮╮
# ┃┈┈┈┣▅╋▅┫┃
# ┃┈┃┈╰━╰━━━━━━╮
# ╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣
# ╲┃┈┈┈┈┈┈┈┈┈┈▉▉▉
# ╲┃┈┈┈┈┈┈┈┈┈┈◥▉◤
# ╲┃┈┈┈┈╭━┳━━━━╯
# ╲┣━━━━━━┫
# ……….
# .……. /´¯/)………….(\¯`\
# …………/….//……….. …\….\
# ………/….//……………....\….\
# …./´¯/…./´¯\……/¯ `\…..\¯`\
# ././…/…/…./|_…|.\….\….\…\.\
# (.(….(….(…./.)..)...(.\.).).)
# .\…………….\/../…....\….\/…………/
# ..\…………….. /……...\………………../
# …..\…………… (………....)……………./     
from sys  import stdin,stdout
from collections  import *
from math import gcd,floor,ceil
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def solve():
    def valid(x,y):
        if x<0 or y<0 or x>=n or y>=m:
            return False 
        if v[x][y]:
            return False
        return True
    
    def DFS(i,j):
        stack=[(i,j)]
        size=1
        v[i][j]=1
        while stack:
            if size==total:
                return
            a,b=stack.pop()
            for p in range(4):
                newA,newB = a+dx[p], b+dy[p]
                if valid(newA,newB):
                    stack.append((newA,newB))
                    size+=1
                    v[newA][newB]=1 
                    if size==total:
                        return
    n,m,k = mp()
    v=[]
    l=[]
    has=0
    for i in range(n):
        s=st()
        x=[0]*m
        for j in range(m):
            if s[j]=='#':
                x[j]=1
                has+=1
        v.append(x)
        l.append(s)
    total = n*m - has - k 
    flag=0 
    #print('to',total)
    for i in range(n):
        for j in range(m):
            if l[i][j]=='.' and not v[i][j]:
                DFS(i,j)
                flag=1
                break
        if flag:
            break

    for i in range(n):
        for j in range(m):
            if not v[i][j] and l[i][j]=='.':
                l[i][j]='X'
    for i in l:
        print(*i,sep='')




     
    
for _ in range(1):
    solve()