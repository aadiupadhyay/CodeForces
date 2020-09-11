for i in range(int(input())):
    s=input()
    l=[0]
    for i in range(len(s)):
        if s[i]=='R':
            l.append(i+1)
    l.append(len(s)+1)
    ans=float('-inf')
    for i in range(1,len(l)):
        ans=max(ans,l[i]-l[i-1])
    print(ans)
