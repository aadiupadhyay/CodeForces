k = int(input())
from collections import deque
d = deque(range(1,10))
 
i = 0
while d:
    l = d.popleft()
    i += 1
    
    if i == k:
        print(l)
        exit()
    
    if l % 10 > 0:
        d.append(l * 10 + l % 10 - 1)
    d.append(l * 10 + l % 10)
    if l % 10 < 9:
        d.append(l * 10 + l % 10 + 1)