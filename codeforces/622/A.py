n=int(input())
x=1
s=1
while (x*(x+1))//2 < n:
  x+=1
  
a= n- (x*(x+1))//2
print(x if a%x==0 else a%x)