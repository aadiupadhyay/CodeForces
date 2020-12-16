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
from math import gcd, floor, ceil, factorial
def st(): return list(stdin.readline().strip())


def li(): return list(map(int, stdin.readline().split()))
def mp(): return map(int, stdin.readline().split())
def inp(): return int(stdin.readline())
def pr(n): return stdout.write(str(n)+"\n")


mod = 1000000007
INF = float('inf')


def ncr3(n):
    if (3 > n or n < 0):
        return 0
    return (n*(n-1)*(n-2))//6


def ncr2(n):
    if (2 > n or n < 0):
        return 0
    return (n*(n-1))//2


def solve():
    n = inp()
    l = li()
    d = Counter(l)
    ans = 0
    for i in d:
        ans += ncr3(d[i])
        ans += ncr2(d[i])*d[i+1]
        ans += d[i]*ncr2(d[i+1])
        ans += d[i]*d[i+1]*d[i+2]
        ans += d[i]*ncr2(d[i+2])
        ans += ncr2(d[i])*d[i+2]

    pr(ans)


for _ in range(inp()):
    solve()
