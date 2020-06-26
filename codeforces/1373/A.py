def solve():
 
    a,b,c=map(int,input().split())
    x,y=-1,-1
    if a<c:
        x=1
    if c//b <a:
        y=b
    print(x,y)
        
 
 
 
 
for _ in range(int(input())):
 
    solve()