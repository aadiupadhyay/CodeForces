s=input()
ans=0
for i in range(3):
    if s[i]=='R':
        c=1
        j=i+1
        while j<3 and s[j]=='R':
            c+=1
            j+=1
        ans=max(ans,c)

print(ans)
