import math
n=int(input())
a=list(map(int,input().split()))
b=[0]*1005
for i in a:
    b[i]+=1
if max(b)<=(math.ceil(n/2)):
    print("YES")
else:
    print("NO")