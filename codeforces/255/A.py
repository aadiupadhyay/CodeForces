from sys  import stdin,stdout

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007

n=inp()
l=li()
c,b,bi=0,0,0
for i in range(n):
    if i%3==0:
        c+=l[i]
    elif i%3==1:
        bi+=l[i]
    else:
        b+=l[i]
x=max(c,b,bi)
if x==c:
    print('chest')
elif x==b:
    pr('back')
else:
    print('biceps')
