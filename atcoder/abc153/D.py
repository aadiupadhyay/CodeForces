n=int(input())
x=1
p=0
while (x<<1)<=n:
  x=x<<1
  p+=1
print(pow(2,p+1)-1)