s=input()
ans=True
a=s[0]
if a!='1':
    print("NO")
else:
    i=1
    c=0
    while i<len(s):
        
        if a=='1':
            if s[i]=='1':
                
                a='1'
                c=0
            elif s[i]=='4':
                
                a='4'
                c+=1
                if c>2:
                    ans=False
                    break
            else:
                ans=False
                break
            
        elif a=='4':
            if s[i]=='4':
            
                c+=1

                if c>2:
                    ans=False
                    break
            elif s[i]=='1':
               
                c=0
                a='1'
            else:
                ans=False
                break
            
        else:
            ans=False
            break
        
        i+=1
        
    if ans:
        print("YES")
    else:
        print("NO")
            
