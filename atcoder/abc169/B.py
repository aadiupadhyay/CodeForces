n=int(input())
l=list(map(int,input().split()))
l.sort()
x=10**18
a=1
for i in l:
  a=a*i
  if a>x:
    a=-1
    break
print(a)