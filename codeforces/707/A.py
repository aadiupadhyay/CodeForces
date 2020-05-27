n,m=map(int,input().split())
c=0
for i in range(n):
    a=input().split()
    if "C" in a or "M" in a or "Y" in a:
        c=1
        break
if c==0:
    print("#Black&White")
else:
    print("#Color")
