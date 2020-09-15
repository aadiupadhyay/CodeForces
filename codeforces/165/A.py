n = int(input())
arr =[]
for i in range(n):
    l = list(map(int,input().split()))
    arr.append(l)
 
ans = 0
for x,y in arr:
    u,l,d,r = 0,0,0,0
    for x1,y1 in arr:
        if x==x1 and y1>y:
            u=1
        elif x==x1 and y1<y:
            d=1
        elif x<x1 and y1==y:
            r=1
        elif x>x1 and y1==y:
            l=1
    if u==d==r==l==1:
        ans+=1
            
print(ans)