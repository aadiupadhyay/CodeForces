def solve():
    n=input()
    for i in range(0,1000,8):
        s=str(i)
        k=0
        for j in n:
            if s[k]==j:
                k+=1
            if k==len(s):
                print('YES')
                print(s)
                return 
    print('NO')
            
        
    
    
for i in range(1):
    solve()