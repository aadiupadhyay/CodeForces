def solve():
    s=input()
    x=""
    x+=s[0]
    for i in range(1,len(s),2):
        x+=s[i]
    print(x)
for _ in range(int(input())):

    solve()
