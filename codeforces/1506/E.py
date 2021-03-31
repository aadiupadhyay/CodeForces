from collections import deque


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    minq, maxq = deque([]), deque([])

    minarr, maxarr = [], []

    maxSeen = 0
    for i in range(n):
        already = arr[i] == maxSeen

        while maxSeen < arr[i]:
            maxSeen += 1
            minq.append(maxSeen)
            maxq.append(maxSeen)

        if already:
            minarr.append(minq.popleft())
            maxarr.append(maxq.pop())
        else:
            minarr.append(minq.pop())
            maxarr.append(maxq.pop())

    print(*minarr)
    print(*maxarr)