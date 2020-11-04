n=int(input())
l=list(map(int,input().split()))
a=l.count(5)
b=n-a
if a>=9 and b>0:
  print((a//9)*9*'5'+ b*'0')
else:
  if b==0:
    print(-1)
  else:
    print(0)