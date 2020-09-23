
def go():
    v = list(map(int, input().split()))
    res = sum(1 if x > 0 else 0 for x in v)
    v = sorted([max(vv-1,0) for vv in v], reverse=True)
    for i in range(3):
        for j in range(i+1,3):
            if v[i]>0 and v[j]>0:
                res+=1
                v[i]-=1
                v[j]-=1
    if all(v):
        res+=1
    return res
 
 
t = int(input())
for _ in range(t):
    print(go())