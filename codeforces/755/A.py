from sys  import stdin,stdout
from  collections import Counter
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

n=inp()
if n==1:
    pr(3)
elif n==2:
    pr(4)
else:
    pr(n-2)
