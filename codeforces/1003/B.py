
n,m,k=map(int,input().split())
if k%2==0 and n>m:
    print('01'*(k//2) +(m-(k//2))*'1' +(n-(k//2))*'0')
elif k%2==0 and n<=m:
    print('10'*(k//2) +(n-(k//2))*'0' +(m-(k//2))*'1')
elif k%2!=0 and n>m:
    print('01'*(k//2) +(n-(k//2))*'0' +(m-(k//2))*'1')
else:
    print('10'*(k//2) +(m-(k//2))*'1' +(n-(k//2))*'0')
