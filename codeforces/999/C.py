n,k=map(int,input().split())
s=input()
l=[0]*26
for i in s:
    l[ord(i)-97]+=1
x=list(l)
i=0
 
while i<26 and k!=0:
    
    if l[i]==0:
        i+=1
        continue
 
    if l[i]>k:
        l[i]-=k
        k=0
        
    else:
        
        k-=l[i]
        l[i]=0
     
    i+=1

z=""
for i in range(len(s)-1,-1,-1):
    if l[ord(s[i])-97]>0:
        z+=s[i]
        l[ord(s[i])-97]-=1
print(z[::-1])
