for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=[]
    if arr[0]<arr[1]:ans.append(arr[0])
    i=1
    while i<n:
        pi=i
        while i<n and arr[i]>arr[i-1]:i+=1
        ans.append(arr[i-1]);i+=1
        if i>=n:break
        while i<n and arr[i]<arr[i-1]:i+=1
        ans.append(arr[i-1])
        i+=1
    if ans[-1]!=arr[-1]:ans.append(arr[-1])
    print(len(ans))
    print(*ans)