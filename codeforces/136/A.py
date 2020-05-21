n=int(input())
l=list(map(int,input().split()))
k=[0]*n
for i in range(n):
    k[l[i]-1]=i+1
print(*k)