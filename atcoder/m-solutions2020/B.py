a,b,c=map(int,input().split())
k=int(input())
x=0
while b<=a:
    b=b<<1
    x+=1
while c<=b:
    c=c<<1
    x+=1
if x<=k:
    print("Yes")
else:
    print("No")
    
