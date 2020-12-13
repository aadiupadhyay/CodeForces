def update(ind, start, end, pos, val):
    if start == end:
        segment[ind] = l[start]
        return
    mid = (start+end)//2
    if pos <= mid:
        update(2*ind+1, start, mid, pos, val)
    else:
        update(2*ind+2, mid+1, end, pos, val)

    segment[ind] = segment[2*ind+1] ^ segment[2*ind+2]


def query(ind, start, end, q1, q2):
    if q1 > end or q2 < start:
        return 0
    if q1 <= start and q2 >= end:
        return segment[ind]
    mid = (start+end)//2
    return query(2*ind+1, start, mid, q1, q2) ^ query(2*ind+2, mid+1, end, q1, q2)


def build(ind, start, end):
    if start == end:
        segment[ind] = l[start]
        return
    mid = (start+end)//2
    build(2*ind+1, start, mid)
    build(2*ind+2, mid+1, end)

    segment[ind] = segment[2*ind+1] ^ segment[2*ind+2]


n, m = map(int, input().split())
l = list(map(int, input().split()))
segment = [0]*(4*n)
build(0, 0, n-1)

for _ in range(m):
    a, b, c = map(int, input().split())
    b -= 1
    if a == 1:
        l[b] ^= c
        update(0, 0, n-1, b, c)

    else:
        c -= 1
        print(query(0, 0, n-1, b, c))
