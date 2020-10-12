from itertools import permutations
ans = []
for i in range(2,10,2):
    temp = [4,7]*(i//2)
    x = list(permutations(temp))
    for j in x:
        t = ''
        for k in j:
            t+=str(k)
        ans.append(int(t))
ans.append(4444477777)
ans.sort()
n = int(input())
for i in ans:
    if i>=n:
        print(i)
        break