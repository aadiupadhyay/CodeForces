for _ in range(int(input())):
    n,k=map(int,input().split())
    s=list(input())
    if set(s)=={'?'}:print('YES');continue
    ans='YES'
    for i in range(n-k):
        if s[i]=='?'==s[i+k]:continue
        if s[i]=='?':s[i]=s[i+k]
        elif s[i+k]=='?':s[i+k]=s[i]
        elif s[i]!=s[i+k]:ans='NO';break
    for i in range(n-k-1,-1,-1):
        if s[i]=='?'==s[i+k]:continue
        if s[i]=='?':s[i]=s[i+k]
        elif s[i+k]=='?':s[i+k]=s[i]
        elif s[i]!=s[i+k]:ans='NO';break
    cz=0
    co=0
    cj=0
    for i in range(k):cz+=s[i]=='0';co+=s[i]=='1';cj+=s[i]=='?'
    if abs(cz-co)>cj:ans='NO'
    for i in range(k,n):
        cz-=s[i-k]=='0'
        co-=s[i-k]=='1'
        cj-=s[i-k]=='?'
        cz+=s[i]=='0'
        co+=s[i]=='1'
        cj+=s[i]=='?'
        if abs(cz-co)>cj:ans='NO'
    print(ans)