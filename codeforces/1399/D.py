import bisect
import math
for _ in range(1):
    for _ in range (int(input())):
        n=int(input())
        s=input()
        zero,one=[],[]
        z,o,x=0,0,1
        ans=[]
        for i in range(n):
            if s[i]=='1':
                if not o<len(one):
                    ans.append(x)
                    zero.append(x)
                    x+=1
                else:
                    ans.append(one[o])
                    zero.append(one[o])
                    o+=1
            else:   
                if not z<len(zero):
                    ans.append(x)
                    one.append(x)
                    x+=1
                else:
                    ans.append(zero[z])
                    one.append(zero[z])
                    z+=1
        print(max(ans))        
        print(*ans)  