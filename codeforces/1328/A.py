import math
for _ in range(int(input())):
    a,b=map(int,input().split())
    z=math.ceil(a/b)
    print(b*z-a)