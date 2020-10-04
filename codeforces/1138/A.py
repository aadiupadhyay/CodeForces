input()
a = b = 1
t = m = 0
for i in input().split():
    if i == t:
        b += 1
    else:
        m = max(min(a, b), m)
        a, b, t = b, 1, i
m = max(min(a, b), m)
print(m * 2)