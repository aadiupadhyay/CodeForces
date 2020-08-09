n = int(input())
ls = list(map(int, input().split()))
xor_sum = 0
for a in ls:
    xor_sum ^=a
 
ans = []
for i in range(n):
    ans.append(str(xor_sum^ls[i]))
    
print(" ".join(ans))