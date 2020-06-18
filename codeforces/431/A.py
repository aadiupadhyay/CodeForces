def solve():
    s=input().split()
    d={}
    for i in range(len(s)):
        d[i+1]=int(s[i])
    ss=input()
    x=0
    for i in ss:
        x+=d[int(i)]
    print(x)
solve()
