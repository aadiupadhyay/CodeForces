# testing
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    ans = 0
    m = int(input())
    k = list(map(int, input().split()))
    for i in range(1, n):
        l[i] += l[i-1]
    for i in range(1, m):
        k[i] += k[i-1]
    print(max(max(l), max(k), 0, max(l)+max(k)))
