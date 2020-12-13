# Aaditya Upadhyay
# ..............
# ╭━┳━╭━╭━╮╮
# ┃┈┈┈┣▅╋▅┫┃
# ┃┈┃┈╰━╰━━━━━━╮
# ╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣
# ╲┃┈┈┈┈┈┈┈┈┈┈▉▉▉
# ╲┃┈┈┈┈┈┈┈┈┈┈◥▉◤
# ╲┃┈┈┈┈╭━┳━━━━╯
# ╲┣━━━━━━┫
# ……….
# .……. /´¯/)………….(\¯`\
# …………/….//……….. …\….\
# ………/….//……………....\….\
# …./´¯/…./´¯\……/¯ `\…..\¯`\
# ././…/…/…./|_…|.\….\….\…\.\
# (.(….(….(…./.)..)...(.\.).).)
# .\…………….\/../…....\….\/…………/
# ..\…………….. /……...\………………../
# …..\…………… (………....)……………./
from sys import stdin, stdout
from collections import *
from math import gcd, floor, ceil
def st(): return list(stdin.readline().strip())


def li(): return list(map(int, stdin.readline().split()))
def mp(): return map(int, stdin.readline().split())
def inp(): return int(stdin.readline())
def pr(n): return stdout.write(str(n)+"\n")


mod = 1000000007
INF = float('inf')


def solve():
    def build(n):
        for i in range(n-1, 0, -1):
            segment[i] = segment[2*i + 1] ^ segment[2*i]

    def query(a, b, n):
        a += n
        b += n
        s = 0
        while a <= b:
            if a & 1:
                s ^= segment[a]
                a += 1
            if b % 2 == 0:
                s ^= segment[b]
                b -= 1
            a = a >> 1
            b = b >> 1
        return s

    def update(ind, val, n):
        ind += n
        segment[ind] ^= val
        while ind > 1:
            ind = ind >> 1
            segment[ind] = segment[2*ind] ^ segment[2*ind+1]
    n, q = mp()
    l = li()
    segment = [0]*(2*n)
    for i in range(n):
        segment[i+n] = l[i]
    build(n)
    ans = []
    for i in range(q):
        a, b, c = mp()
        b -= 1
        if a == 2:
            c-=1
            A = query(b, c, n)
            ans.append(A)
        else:
            update(b, c, n)
    print('\n'.join(map(str, ans)))


for _ in range(1):
    solve()
