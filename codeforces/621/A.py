n=int(input())
l=list(map(int,input().split()))
s=sum(l)
if s%2==0:
    print(s)
else:
    l.sort()
    for  i in l:
        if i&1:
            s-=i
            print(s)
            break
        
        
