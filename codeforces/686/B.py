
n=int(input())
ans=0
l=list(map(int,input().split()))

s=sorted(l)

for i in range(n):

    if l[i]!=s[i]:
        

        a=l[i+1:].index(s[i])
        ind=i+a+1

        while ind!=i:
            print(ind,ind+1)
            l[ind-1],l[ind]=l[ind],l[ind-1]
            ind-=1

  
    
