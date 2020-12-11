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
    n, m = mp()
    l = []
    ans = 0
    prefix = []
    for i in range(n):
        s = st()
        val = [0]*m
        if s[0] == '.':
            val[0] = 1
        else:
            ans += 1
        for j in range(1, m):
            if s[j] == '*':
                ans += 1
                val[j] = val[j-1]
            else:
                val[j] = 1+val[j-1]
        l.append(s)
        prefix.append(val)
    for i in range(n):
        for j in range(m):
            if l[i][j] == '*':
                x, y, height = j-1, j+1, i+1
                while height < n and x >= 0 and y < m:
                    if x == 0:
                        cur = prefix[height][y]
                    else:
                        cur = prefix[height][y] - prefix[height][x-1]
                    if cur > 0:
                        break
                    else:
                        ans += 1
                        x -= 1
                        y += 1
                        height += 1
    pr(ans)


for _ in range(inp()):
    solve()
