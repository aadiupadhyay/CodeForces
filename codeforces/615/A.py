n,m=map(int,input().split())
k=[0]*m
for i in range(n):
    l=list(map(int,input().split()))
    l=l[1:]
    for _ in l:
        k[_-1]=1
        #print(k)
if k.count(1)==m:
    print("YES")
else:
    print("NO")
