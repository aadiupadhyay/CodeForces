a, b, c, d = sorted(map(int, input().split()))
if b+c == a+d or a+b+c == d:
    print("YES")
else:
    print("NO")
