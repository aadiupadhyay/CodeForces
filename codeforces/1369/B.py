def solve():

    n=int(input())
    s=input()
    x=[i for i in s]
    p=sorted(x)
    count=0
    if x==p:
        count=1
        print(s)
        return 
        
    c,d=0,0
    for i in s:
        if i=='1':
            break
        c+=1
    for i in reversed(range(n)):
        if s[i]=='0':
            break
        d+=1
    
    if count==0:
        print('0'*(c+1)+'1'*d)
    
    
    

for _ in range(int(input())):

    solve()
