def solve():
 
    s=input()
    i,c=0,0
    while i<len(s)-1:
        if (s[i]=='1' and s[i+1]=='0') or (s[i]=='0' and s[i+1]=='1'):
 
            if i+2 < len(s):
                s=s[:i]+s[i+2:]
            else:
                s=s[:i]
 
            c+=1
            i=0
        else:
            i+=1
    if c%2:
        print("DA")
    else:
        print("NET")
            
 
 
 
for _ in range(int(input())):
 
    solve()
