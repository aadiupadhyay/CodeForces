import sys
input = sys.stdin.readline
 
 
def solve(cnt, l, r):
    if r - l == 1:
        if s[l] == alph[cnt]:
            return 0
        return 1
    mid = (l + r) // 2
    tmp1 = solve(cnt + 1, l, mid) + (r - mid - s[mid:r].count(alph[cnt]))
    tmp2 = solve(cnt + 1, mid, r) + (mid - l - s[l:mid].count(alph[cnt]))
    return min(tmp1, tmp2)
 
 
t = int(input())
INF = 10 ** 18
alph = "abcdefghijklmnopqrstuvwxyz"
 
for _ in range(t):
    n = int(input())
    s = input()[:-1]
    print(solve(0, 0, n))