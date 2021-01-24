'''
Aaditya Upadhyay
                          ud$$$**$$$$$$bc.
                       u@**"        4$$$$$$Nu
                     J                ""#$$$$$r
                    @                       $$$b
                  .F                        ^*3$$$
                 :% 4                         J$$N
                 $  :F                       :$$$$$
                4F  9                       J$$$$$$$
                4$   k             4$$$bed$$$$$$$$$
                $r  'F            $$$$$$$$$$$$$$$$r
                $$$   b.           $$$$$$$$$$$$$$$$N
                $$$$k 3eeed$b    $$Euec."$$$$$$$$$
 .@$**N.        $$$$$" $$$$$F'L $$$$$$$$$$$  $$$$$$$
 :$L  'L       $$$$$ 4$$$$$$  * $$$$$$$$$F  $$$$$F         edNc
@$$$N  ^k      $$$$$  3$$$$*%   F4$$$$$$$   $$$$$"        d"  zN
$$$$$$   ^k     '$$$"   #$$F   .$  $$$$c.u@$$$          J"  @$$$r
$$$$$$b   *u    ^L            $$  $$$$$$$$$$$u@       $$  d$$$$$$
 ^$$$$$$.    "NL   "N. z@*     $$$  $$$$$$$$$$$$P      P  d$$$$$$$
    ^"*$$$b   '*L   9E      4$$$  d$$$$$$$$$$$"     d*   J$$$$r
         ^$$$u  '$.  $$L     "#" d$$$$$$".@$$    .@$"  z$$$$*"
           ^$$$$. ^N.3$$$       4u$$$$$$$ 4$$$  u$*" z$$$"
             '*$$$$$$$$ *b      J$$$$$$b u$P $"  d$P
                # $$$$$$ 4$ 3*$"$*$ $"$'c@@$$$$ .u@$$P
                  "$$$$  ""F~$ uNr$$$^&J$$$F $$$$#
                    "$$    "$$bd$.W$$$$$$$F $$"
                      ?k         ?$$$$$$$$$$F'*
                       9$bL     z$$$$$$$$$$F
                        $$$$    $$$$$$$$$$$$$
                         '#$c  '$$$$$$$$$"
                          .@"#$$$$$$$$$$$b
                        z*      $$$$$$$$$$$N.
                      e"      z$$"  #$$k  '*$$.
                  .u*      u@P"      '#$c   "$c
           u@$*"""       d$$"            "$$u  ^*$b.
         :F           JP"                ^$$c   '"$$$$$bL
        d$$  ..      @$#                      #$b         '#$
        9$$$$$b   4$$                          ^$k         '$
         "$""b u$$                             '$    d$$$$P
           'F $$$$$"                              ^b  ^$$$b$
            'W$$$$"                                'b@$$$$"
                                                     ^$$$*
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
    n, x = mp()
    val = 0
    x *= 100
    for i in range(1, n+1):
        a, b = mp()
        val += a*b
        if val > x:
            print(i)
            return
    pr(-1)


for _ in range(1):
    solve()
