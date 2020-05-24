n=int(input())
a,b,c=0,0,0
for i in range(n):
    l=list(map(int,input().split()))
    a+=l[0]
    b+=l[1]
    c+=l[2]
if a==0 and b==0 and c==0:
    print("YES")
else:
    print("NO")
    
