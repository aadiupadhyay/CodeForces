
def solve():
    n=int(input())
    s=input()
    ss=input()
    c=0
    for i in range(n):
        a,b=int(s[i]),int(ss[i])
        c+=min(abs(a-b),10-abs(a-b))

    print(c)

solve()
