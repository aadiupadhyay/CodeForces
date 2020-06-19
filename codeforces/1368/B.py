def solve():
    n=int(input())
    l=[1]*10
    s="codeforces"
    prod=1
    j=0
    while prod<n:
        l[j]+=1
        j=(j+1)%10
        prod=1
        for i in range(10):
            prod*=l[i]
    for i in range(10):
        print(s[i]*l[i],end="")
        
solve()
