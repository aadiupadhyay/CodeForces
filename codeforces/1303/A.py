def solve():

    s=input()
    x=s[::-1]
    if s.count('1')==0:
        print("0")
    else:
        a=s.index('1')
        b=len(s)-1-x.index('1')
        print(s[a:b+1].count('0'))
            

        
for _ in range(int(input())):
    solve() 
