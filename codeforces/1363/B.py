import sys
 
readline = sys.stdin.readline
 
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
 
def solve():
    s = list(map(int, list(ns())))
    n = len(s)
    g = sum(s)
    c = 0
    ans = min(g, n-g)
    for i in range(n):
        c += s[i]
        ans = min(ans, c + n-1-i-g+c, i+1-c + g-c)
    print(ans)
    return
 
# solve()
 
T = int(input())
for _ in range(T):
    solve()