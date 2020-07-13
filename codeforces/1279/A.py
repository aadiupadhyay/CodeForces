for _ in range(int(input())):

    c=0
    l=list(map(int,input().split()))
    l.sort()
    if l[0]+l[1]+1 < l[2]:
        print("No")
    else:
        print("Yes")
    
            
        
        
        
