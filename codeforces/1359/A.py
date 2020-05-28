import math
for _ in range(int(input())):
    n,m,k=map(int,input().split())
    if n//k>=m:
        print(m)
    else:
        a=m-(n//k)
        print(n//k -math.ceil(a/(k-1)))
