n=int(input())
l=list(map(int,input().split()))
l.sort()
print(min(l[-1]-l[1],l[-2]-l[0]))
    
        
