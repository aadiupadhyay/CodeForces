for _ in range(1):
    n=int(input())
    x=''
    if n==1:
        print('a')
        
    else:
        for i in range(0,n//2 ):
            if i&1:
                x+='aa'
            else:
                x+='bb'
        if len(x)==n:
            print(x)
        else:
            a=n-len(x)
            if x[-1]=='a':
                x+='b'*a
            else:
                x+='a'*a
            print(x)
