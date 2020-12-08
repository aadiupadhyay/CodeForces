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
    s = st()
    if n % 4:
        pr('===')
        return
    d = Counter(s)
    a = n//4
    for i in d:
        if i != '?':
            if d[i] > a:
                pr('===')
                return
    A = a-d['A']
    C = a-d['C']
    G = a-d['G']
    T = a-d['T']
    for i in range(n):
        if s[i] == '?':
            if A:
                s[i] = 'A'
                A -= 1
            elif T:
                s[i] = 'T'
                T -= 1
            elif G:
                s[i] = 'G'
                G -= 1
            elif C:
                s[i] = 'C'
                C -= 1
    print(''.join(s))


for _ in range(1):
    solve()
