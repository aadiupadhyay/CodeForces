n,m=map(int,input().split())
l=[]
ans=[]
a=0
for i in range(n):
    s=input()
    x=''
    l.append(s)
    if a==0:
        st='B'
        pt='W'
    else:
        st='W'
        pt='B'
    for i in range(m):
        if i%2==0:
            if s[i]=='-':
                x+='-'
            else:
                x+=st
        else:
            if s[i]=='-':
                x+='-'
            else:
                x+=pt
    a^=1
    ans.append(x)
for i in ans:
    print(*i,sep='')
            
            
    

        
        
