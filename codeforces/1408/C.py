from sys import stdin
def solve():
    n, l = map(int, stdin.readline().split())
    a = map(int, stdin.readline().split())
    x, y = 0, n - 1
    u = v = 1.
    p, q = 0, l
    t = 0
    while y >= x:
        w = (a[x] - p) / u
        z = (q - a[y]) / v
        if w < z:
            t += w
            u += 1
            p = a[x]
            q -= v * w
            x += 1
        else:
            t += z
            v += 1
            q = a[y]
            p += u * z
            y -= 1
    print "%.12f" % (t + (q - p) / (u + v))

T = int(stdin.readline())
for _ in xrange(T):
    solve()
