from math import gcd
y,w=map(int,input().split())
ans=6-max(y,w)+1
g=gcd(6,ans)
if g==0:print('0/1')
else:print(str(ans//g)+'/'+str(6//g))