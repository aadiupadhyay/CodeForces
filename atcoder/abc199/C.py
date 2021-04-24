import sys
import io, os
input = sys.stdin.readline
#input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

n = int(input())
s = str(input().rstrip())

S = s[0:n]
T = s[n:]

S = list(S)
T= list(T)

q = int(input())
for i in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        a, b = a-1, b-1
        if a <= n-1 and b <= n-1:
            S[a], S[b] = S[b], S[a]
        elif a <= n-1 and n-1 < b:
            S[a], T[b-n] = T[b-n], S[a]
        else:
            T[a-n], T[b-n] = T[b-n], T[a-n]
    else:
        S, T = T, S
print(''.join(S)+''.join(T))
