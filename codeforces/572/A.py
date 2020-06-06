a,b=map(int,input().split())
n,k=map(int,input().split())
l=list(map(int,input().split()))
p=list(map(int,input().split()))
if l[n-1]<p[b-k]:
    print("YES")
else:
    print("NO")