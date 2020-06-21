n=int(input())
s=input()
i=0
x=0
while i<n:
    if s[i]=="x":
        c=1
        j=i+1
        while j<n and s[j]=="x":
            j+=1
            c+=1
        if c>2:
            x+=c-2
        i=j
    else:
        i+=1
print(x)
            
    
