import sys

# D - Snuke Prime
N, C = map(int, input().split())
dic = dict()

for _ in range(N):
  a, b, c = map(int, input().split())

  dic.setdefault(a, 0)
  dic[a] += c

  dic.setdefault(b+1, 0)
  dic[b+1] -= c

# 戻り値は二次元リスト
days = sorted(dic.items())

cusum = 0
ans = 0
prev = 0

for d in days:
  if d[0] > prev + 1:
    if cusum > C:
      ans += C * (d[0]-prev-1)
    else:
      ans += cusum * (d[0]-prev-1)

  prev = d[0]

  cusum += d[1]

  if cusum > C:
    ans += C
  else:
    ans += cusum

print(ans)