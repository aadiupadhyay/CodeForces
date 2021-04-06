
# for divyanshu

def solve():

    s = list(input())
    n = len(s)
    a1 = 0
    for i in range(1, n):
        if s[i] == s[i-1]:
            a1 += 1
            for j in 'abcdefghijklmnopqrstuvwxyz':
                if i+1 < n:
                    if s[i] != j and s[i+1] != j:
                        s[i] = j
                        break
                else:
                    if s[i] != j:
                        s[i] = j
                        break
    print(*s, sep='')


for _ in range(1):
    solve()
