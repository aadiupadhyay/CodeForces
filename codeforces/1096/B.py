n = int(input())
st = input()
l = 0
while st[l] == st[l + 1]:
    l += 1
r = n - 1
while st[r] == st[r - 1]:
    r -= 1
ans = l + 1 + (n - r) + 1
if st[r] == st[l]:
    ans += (l + 1) * (n - r)
print(ans % 998244353)