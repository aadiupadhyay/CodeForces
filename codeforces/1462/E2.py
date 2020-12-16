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


def compute(ma):
    fact = [0 for i in range(ma)]
    invfact = [0 for i in range(ma)]
    fact[0] = 1
    for i in range(1, ma):
        fact[i] = (i % mod * fact[i-1] % mod) % mod

    invfact[ma-1] = pow(fact[ma-1], mod-2, mod)
    for i in range(ma-2, -1, -1):
        invfact[i] = (invfact[i+1] % mod * (i+1) % mod) % mod

    return fact, invfact


fact, invfact = compute(2*10**5 + 1)


def ncr(n, r):
    if (r > n or n < 0 or r < 0):
        return 0
    return ((fact[n] % mod * invfact[r] % mod) % mod * (invfact[n-r] % mod) % mod) % mod


def solve():
    n, m, k = mp()
    l = li()
    l.sort()
    ans = 0
    left, right = 0, 0
    while right < n:
        if l[right]-l[left] <= k:
            size = right-left+1
            if size >= m:
                value = ncr(size-1, m-1)
                ans = (ans % mod + value % mod) % mod
            right += 1
        else:
            left += 1
    pr(ans)


for _ in range(inp()):
    solve()
