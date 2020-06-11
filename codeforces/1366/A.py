import math
for _ in range(int(input())):
    a,b=map(int,input().split())
    if a==0 or b==0:
        print("0")
        continue
    print(min(a,b,(a+b)//3))
