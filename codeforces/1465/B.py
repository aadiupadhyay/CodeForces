'''
Aaditya Upadhyay

                          oooo$$$$$$$$$$$
                          
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
  o$$
  $$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$"$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$""""""""
 """"       $$$$    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"      o$$$
            "$$o     """$$$$$$$$$$$$$$$$$$"$$"         $$$
              $$o          "$$""$$$$$$""""           o$$$
               $$$o                                o$$$"
                "$$$o      o$$$$$o"$$$o        o$$$$
                  "$$$$oo     ""$$$o$$$$o   o$$$$""
                     ""$$$$
                       "$$o$$$$$$$$$"""
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
    def check(n):
        temp = n
        while temp:
            x = temp % 10
            temp //= 10
            if x != 0:
                if n % x != 0:
                    return False
        return True

    n = inp()
    while True:
        if check(n):
            pr(n)
            return
        n += 1


for _ in range(inp()):
    solve()
