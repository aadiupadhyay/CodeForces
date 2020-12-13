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
    l = li()
    d = Counter(l)
    ans = 0
    x = len(d)
    for i in d:
        cur = d[i]
        ans = max(ans, min(cur, x-1))
        ans = max(ans, min(cur-1, x))
    pr(ans)


for _ in range(inp()):
    solve()
