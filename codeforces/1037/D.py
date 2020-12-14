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
    n = inp()
    l = [li() for i in range(n-1)]
    d = {i: [] for i in range(1, n+1)}
    for i in l:
        a, b = i
        d[a].append(b)
        d[b].append(a)

    stack = [1]
    par = [0 for i in range(n+1)]
    visited = [0 for i in range(n+1)]
    visited[1] = 1
    while stack:
        a = stack.pop()
        for i in d[a]:
            if not visited[i]:
                visited[i] = 1
                par[i] = a
                stack.append(i)
    l = li()
    if l[0] != 1:
        pr('No')
        return
    x = Counter(par)
    i = 0
    j = 1
    while i < n:
        p = x[l[i]]
        if p == 0:
            i += 1
        else:
            c = 0
            while c < p:
                if par[l[j+c]] != l[i]:
                    pr('No')
                    return
                c += 1
            j += p
            i += 1
    pr('Yes')


for _ in range(1):
    solve()
