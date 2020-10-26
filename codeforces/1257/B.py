import sys
 
readline = sys.stdin.readline
readlines = sys.stdin.readlines
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')
 
 
def solve():
    x, y = nm()
    if x == 1 and y > 1 or x < 4 and y > 3:
        print('NO')
    else:
        print('YES')
    return
 
# solve()
 
T = ni()
for _ in range(T):
    solve()
