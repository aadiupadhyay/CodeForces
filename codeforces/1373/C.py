t=int(input())
for i in range(t):
    s=input()
    n=len(s)
    cur=0
    r=0
    j=0
    while(j<n):
        if s[j]=="+":
            cur+=1
        else:
            cur-=1
        r+=1
        if cur<0:
            cur=0
            r+=(j+1)
        j+=1
    print(r)