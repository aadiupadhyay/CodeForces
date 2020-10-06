n=int(input())
a= list(map(int, input().split()))
 
x=[n]*100001
for i in range(n):
    x[a[i]-min(n-i-1,i)]-=1
print (min(x[1:]))