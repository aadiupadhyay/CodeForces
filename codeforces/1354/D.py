from sys import stdin, gettrace
from array import array

# if not gettrace():
#     def input():
#         return next(stdin)[:-1]


def input():
   return stdin.buffer.readline()

def main():
    n,q = map(int, input().split())
    aa = array('i')
    qq = array('i')
    buffer = stdin.buffer.readline(40960)
    while buffer:
        if len(buffer) < 40960:
            aa.extend(map(int, buffer.split()))
            break
        j = buffer.rfind(b' ')
        if j == -1:
            j = len(buffer)
        aa.extend(map(int, buffer[:j].split()))
        buffer = buffer[j+1:] + stdin.buffer.readline(40960)
    buffer = stdin.buffer.readline(40960)
    while buffer:
        if len(buffer) < 40960:
            qq.extend(map(int, buffer.split()))
            break
        j = buffer.rfind(b' ')
        if j == -1:
            j = len(buffer)
        qq.extend(map(int, buffer[:j].split()))
        if buffer[-1] == b'\n':
            break
        buffer = buffer[j+1:] + stdin.buffer.readline(40960)

    le = array('i')
    c = 0
    lec = 0
    for a in aa:
        if a > c:
            for _ in range(c, a):
                le.append(lec)
                c = a
        lec += 1
    for i in range(c, n+2):
        le.append(lec)

    def count_le(v):
        res = le[v]
        for q in qq:
            if q > 0 and q <= v:
                res += 1
            elif q < 0 and -q <= res:
                res -= 1
        return res

    if count_le(n+1) == 0:
        print(0)
        return

    if n == 1:
        print(1)
        return

    r = n
    l = 0
    while r - l > 1:
        mid = (r + l)//2
        if count_le(mid) > 0:
            r = mid
        else:
            l = mid
    print(r)
    return

if __name__ == "__main__":
    main()