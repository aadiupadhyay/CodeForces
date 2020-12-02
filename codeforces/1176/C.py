import sys
input = sys.stdin.readline
from collections import *
 
n = int(input())
a = list(map(int, input().split()))
cnt = [0]*5
ans = 0
    
for ai in a:
    if ai==4:
        cnt[0] += 1
    elif ai==8:
        if cnt[0]>=1:
            cnt[0] -= 1
            cnt[1] += 1
        else:
            ans += 1
    elif ai==15:
        if cnt[1]>=1:
            cnt[1] -= 1
            cnt[2] += 1
        else:
            ans += 1
    elif ai==16:
        if cnt[2]>=1:
            cnt[2] -= 1
            cnt[3] += 1
        else:
            ans += 1
    elif ai==23:
        if cnt[3]>=1:
            cnt[3] -= 1
            cnt[4] += 1
        else:
            ans += 1
    elif ai==42:
        if cnt[4]>=1:
            cnt[4] -= 1
        else:
            ans += 1
        
ans += cnt[0]+2*cnt[1]+3*cnt[2]+4*cnt[3]+5*cnt[4]
print(ans)
