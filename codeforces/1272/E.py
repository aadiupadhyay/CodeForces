from collections import deque
n = int(input())
a = [int(x) for x in input().split()]
d = [-1] * n
line = [[] for i in range(n)]
for i in range(n):
    for j in [i-a[i], i+a[i]]:
        if (0 <= j < n):
            if (a[i] % 2 == a[j] % 2):
                line[j].append(i)
            else:
                d[i] = 1
    
q = deque()
for i in range(n):
    if (d[i] == 1):
        q.append(i)
while (q):
    t = q.popleft()
    for i in line[t]:
        if (d[i] == -1):
            d[i] = d[t] + 1
            q.append(i)
print(*d)
