import math
x,y=map(int,input().split())
a=x*(math.log(y,10))
b=y*(math.log(x,10))
if a>b:
  print('<')
elif a<b:
  print('>')
else:
  print('=')