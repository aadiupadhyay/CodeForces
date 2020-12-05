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
from sys  import stdin,stdout
from collections  import *
from math import gcd,floor,ceil
from bisect import bisect_right
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

def solve():
    def BIN(l,x):
        left,right =0,n-1
        while left<=right:
            mid= (left+right)>>1
            if l[mid]>x and (l[mid-1]<=x or mid==0):
                return mid
            if l[mid]<=x:
                left=mid+1
            else:
                right=mid-1
        return left
        
    n,q = mp()
    l=li()
    k=li()
    l.sort()
    ans=[BIN(l,i) for i in k]
    print(*ans)
    
for _ in range(1):
    solve()