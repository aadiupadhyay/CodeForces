t = int(input())
for _ in range(t):
    b, p, f = map(int, input().split())
    h, c = map(int, input().split())
    x = b//2
    ans= 0
    for i in range(x+1):
        j = x-i
        temp = h*min(p, i)+c*min(f, j)
        ans = max(ans, temp)
    print(ans)