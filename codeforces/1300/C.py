R = lambda: list(map(int, input().split()))
n = int(input())
a = R()
first = 0
for i in range(30, -1, -1):
    cnt = 0
    for j in range(n):
        if a[j] & 1 << i:
            cnt += 1
            first = j
    if cnt == 1:
        break
print(a[first], *(a[:first]), *(a[first + 1:]))