n=int(input())
l=list(map(int,input().split()))
a=max(l)
s=0
for i in l:
    s+=(a-i)
print(s)
            
        
