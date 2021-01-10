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
    n, k = mp()
    l = li()
    ans = []
    i = 0
    while i < n:
        j = i
        x = [l[i], 0]
        while j < n and l[j] == l[i]:
            j += 1
            x[1] += 1
        i = j
        ans.append(x)
    i = 0
    val = 0
    while i < len(ans) and ans[i][0] % k == 0:
        val += ans[i][0]*ans[i][1]
        ans.append([ans[i][0]//k, ans[i][1]*k])
        i += 1
    while i < len(ans):
        val += ans[i][0]*ans[i][1]
        i += 1
    pr(val)


for _ in range(inp()):
    solve()
