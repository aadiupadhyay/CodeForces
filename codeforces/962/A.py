n=int(input())
l=list(map(int,input().split()))
s=sum(l)
s=s//2 + s%2
a=0
for i in range(n):
  a+=l[i]
  if a>=s:
    print(i+1)
    break