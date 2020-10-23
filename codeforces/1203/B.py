def solve(arr,n,ans):
    arr.sort()
    products = set()
    start = 0
    end = 4*n-1
    while start < end:
        if arr[start] != arr[start+1]:
            ans.append('NO')
            return
        if arr[end] != arr[end-1]:
            ans.append("NO")
            return
        p = arr[start]*arr[end]
        if p not in products:
            if len(products) == 0:
                products.add(p)
            else:
                ans.append('NO')
                return

        start += 2
        end -= 2

    ans.append('YES')

def main():
    q = int(input())
    ans = []
    for i in range(q):
        n = int(input())
        arr = list(map(int,input().split()))
        solve(arr,n,ans)

    for i in ans:
        print(i)

main()
