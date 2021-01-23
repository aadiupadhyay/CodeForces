'''
Aaditya Upadhyay

                          oooo$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $o$
oo $ $ "$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$o       $$o$o$
"$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  """$$$
   "$$$""""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$o
   o$$"   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" "$$$$$ooooo$$$o
  o$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$"$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$""""""""
 """"       $$$$    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"      o$$$
            "$$o     """$$$$$$$$$$$$$$$$$$"$$"         $$$
              $$o          "$$""$$$$$$""""           o$$$
               $$$o                                o$$$"
                "$$$o      o$$$$$o"$$$o        o$$$$
                  "$$$$oo     ""$$$o$$$$o   o$$$$""
                     ""$$$$oooo  "$$o$$$$$$$$$"""
                        ""$$$$$$oo $$$$$$$$$$
                                """"$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$"
                                      "$$$""""

'''

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
    NSR = [n for i in range(n)]
    NSL = [-1 for i in range(n)]
    s = []
    ss = []
    for i in range(n-1, -1, -1):
        if not s:
            s.append(i)
        else:

            while s and l[s[-1]] >= l[i]:
                s.pop()
            if s:
                NSR[i] = s[-1]
            s.append(i)
        cur = n-1-i
        if not ss:
            ss.append(cur)
        else:
            while ss and l[ss[-1]] >= l[cur]:
                ss.pop()
            if ss:
                NSL[cur] = ss[-1]
            ss.append(cur)
    ans = 0
    for i in range(n):
        cur = (NSR[i]-NSL[i]-1)*l[i]
        ans = max(ans, cur)
    pr(ans)


for _ in range(1):
    solve()
