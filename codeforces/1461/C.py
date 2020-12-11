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
    n, q = mp()
    l = li()
    c = 0
    x = []
    for i in range(q):
        a, b = input().split()
        b = float(b)
        a = int(a)
        x.append((a, b))
    if sorted(l) == l:
        pr(1)
        return
    p = n-1
    k = n
    v = []
    while p >= 0:
        if l[p] != k:
            break
        else:
            p -= 1
            k -= 1
    p += 1
    for i in range(q):
        x1, y1 = x[i]
        if x1 >= p:
            v.append(y1)
    ans = 1
    # print(v)
    for i in v:
        ans *= (1-i)
    pr(1-ans)


for _ in range(inp()):
    solve()
