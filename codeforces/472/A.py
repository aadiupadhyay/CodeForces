def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

n=int(input())
if n%2==0:
    print(4,n-4)
else:
    for i in range(4,n//2+1):
        if not prime(i) and not prime(n-i):
            break
    print(i,n-i)
            
