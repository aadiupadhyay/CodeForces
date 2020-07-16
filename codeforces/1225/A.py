a,b=map(int,input().split())
if a==b:
    print(str(a)+'1',str(b)+'2')
elif a==9 and b==1:
    print(a,str(b)+'0')
elif b-a>1 or b<a:
    print("-1")
elif a+1==b:
    print(str(a)+'9',str(b)+'0')
    
