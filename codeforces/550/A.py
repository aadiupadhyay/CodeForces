s = input()
abc = [0,0,0]
n = len(s)
i=0
while(i<n):
    # print(i)
    ch = s[i]
    if(ch=='A'):
        if(i<n-1 and s[i+1]=='B'):
            if(i<n-2 and s[i+2]=='A'):
                abc[2] += 1
                i+=3
            else:
                abc[0] = 1
                i+=2
        else:
            i+=1
    elif(ch=='B'):
        if(i<n-1 and s[i+1]=='A'):
            if(i<n-2 and s[i+2]=='B'):
                abc[2] += 1
                i+=3
            else:
                abc[1] = 1
                i+=2
        else:
            i+=1
    else:
        i+=1
# print(abc)
if(abc[0]==1 and abc[1]==1):
    print("YES")
elif(abc[2]!=0 and max(abc[0], abc[1])!=0):
    print("YES")
elif(abc[0]==0 and abc[1]==0 and abc[2]>=2):
    print("YES")
else:
    print("NO")