import sys, os

big = 10**7 + 10

def solve():
    summer = [1] * big
    for i in range(2, big):
        j = i
        while j < big:
            summer[j] += i
            j += i
    return summer

summer = solve()

mapper = [-1] * big
for i in reversed(range(1, big)):
    if summer[i] < big:
        mapper[summer[i]] = i

inp = [int(x) for x in sys.stdin.buffer.read().split()]

os.write(1, b'\n'.join(str(mapper[c]).encode('ascii') for c in inp[1:]))