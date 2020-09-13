ans = [0]*2001
for i in range(3, 6):
    ans[i] = 1
 
for i in range(6, 2001):
    tmp = i - 3
    ans[i] = (sum(ans[3:tmp+1])+1)%(10**9+7)
    
print(ans[int(input())])