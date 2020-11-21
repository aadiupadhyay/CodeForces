from sys  import stdin,stdout
from collections  import *
from math import gcd,floor,ceil
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

def solve():
    n=inp()
    s=st()
    stack=[]
    for i in s:
        if len(stack)<2:
            stack.append(i)
        else:
            if i=='x' and stack[-1]=='o' and stack[-2]=='f':
                stack.pop()
                stack.pop()
            else:
                stack.append(i)
    pr(len(stack))
solve()