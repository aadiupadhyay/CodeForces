for i in range(5):
    l=list(map(int,input().split()))
    if 1 in l:
        x,y=i+1,l.index(1)+1
print(abs(3-x)+abs(3-y))