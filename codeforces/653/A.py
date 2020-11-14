input()
T = set(map(int, input().split()))

print('YES' if any(t-1 in T and t+1 in T for t in T) else 'NO')