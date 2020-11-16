import itertools
 
N, K = map(int, input().split())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))
 
cnt = 0
for i in itertools.permutations(range(1, N)):
    ans = 0
    for j in range(N-1):
        if j == 0:
            ans += A[0][i[0]]
        else:
            ans += A[i[j-1]][i[j]]
    ans += A[i[-1]][0]
    if ans == K:
        cnt += 1
 
print(cnt)