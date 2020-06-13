for _ in range(int(input())):
    a,b=map(int,input().split())
    c=0
    x=60-b
    a+=1
    c+=x+(24-a)*60
    print(c)
    
