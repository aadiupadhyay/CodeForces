n,m=map(int,input().split())
mid=''
l=set()
start=''
end=''
for i in range(n):
    s=input()
    if s==s[::-1]:
        if mid=='':
            mid+=s
    else:
        if s[::-1] in l:
            start+=s
            end=s[::-1]+end
            l.discard(s)

        else:
            l.add(s)

f=start+mid+end
print(len(f))

print(f)
            
        
