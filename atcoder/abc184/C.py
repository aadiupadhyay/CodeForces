def solve():
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    if x1==x2 and y1==y2:
        return 0
    if x1+y1 == x2+y2:
        return 1
    if x1-y1 == x2-y2:
        return 1 
    if abs(x1-x2) + abs(y1-y2) <= 3:
        return 1
    if (x1+y1)%2 == (x2+y2)%2:
        return 2
    if abs(x2-y2+y1-x1) / 2**0.5 <= 3:
        return 2
    if abs(x2+y2-y1-x1) / 2**0.5 <= 3:
        return 2
    if abs(x1-x2) + abs(y1-y2) <= 6:
        return 2
    return 3
 
print(solve())