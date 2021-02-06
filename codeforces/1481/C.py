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
    n, m = mp()
    a = li()
    b = li()
    c = li()
    if c[-1] not in b:
        pr('NO')
        return
    last = c[-1]
    index = -1
    for i in range(n):
        if b[i] == last:
            index = i
            break
    ans = [-1 for i in range(m)]
    graph = [[] for i in range(n+1)]
    for i in range(n):
        if a[i] != b[i]:
            graph[b[i]].append(i+1)
    if graph[last]:
        ans[-1] = graph[last].pop()
        index = ans[-1]-1
    else:
        ans[-1] = index+1
    for i in range(m-1):
        if graph[c[i]]:
            ans[i] = graph[c[i]].pop()
        else:
            ans[i] = index+1
    if all(not graph[i] for i in range(n+1)):
        pr('YES')
        print(*ans)
        return
    pr('NO')


for _ in range(inp()):
    solve()
