
n = int(input())
a = list(map(int, input().split()))[1:]
b = list(map(int, input().split()))[1:]
s = set(a)
t = set(b)
k = s.union(t)
yes = 0
for i in range(1, n+1):
    if i in k:
        yes = 1
    else:
        yes = 0
        break
if(yes == 1):
    print('I become the guy.')
else:
    print('Oh, my keyboard!')