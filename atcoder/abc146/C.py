A, B, X = map(int, input().split())
l = 0
r = 10 ** 9 + 1
while l + 1 < r:
  c = (l + r) // 2
  x = A * c + B * len(str(c))
  if x <= X:
    l = c
  else:
    r = c
print(l)