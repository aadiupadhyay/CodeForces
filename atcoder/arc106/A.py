from sys  import stdin,stdout
from collections import *
from math import *
st = lambda:list(stdin.readline().strip())
li = lambda:list(map(int,stdin.readline().split()))
mp = lambda:map(int,stdin.readline().split())
inp = lambda:int(stdin.readline())
pr = lambda n: stdout.write(str(n)+"\n")

def solve():
    n=inp()
    for i in range(1,100):
        for j in range(1,100):
            if 3**i + 5**j ==n:
                print(i,j)
                return
    pr(-1)

solve()






    
