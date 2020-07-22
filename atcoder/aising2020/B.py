n=int(input())
c=0
l=list(map(int,input().split()))
for i in range(0,n,2):
  if l[i]&1:
    c+=1
print(c)