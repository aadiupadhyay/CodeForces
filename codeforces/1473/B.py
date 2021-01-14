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
                #$$$$$$ 4$ 3*$"$*$ $"$'c@@$$$$ .u@$$P
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
    s = input()
    k = input()
    n, m = len(s), len(k)
    lcm = n*m // gcd(n, m)
    a, b = lcm-n, lcm-m
    s += a//n * s + s[:a % n]
    k += b//m*k + s[:b % m]
    if s == k:
        print(s)
    else:
        pr(-1)


for _ in range(inp()):
    solve()
