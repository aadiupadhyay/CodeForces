n = int(input())
a = list(map(int,input().split()))

rises = [False for _ in range(n-1)]

balance = 1000


for i in range(n-1):
    if a[i+1] > a[i]:
        rises[i] = True

for i in range(n-1):
    if rises[i]:
        purchase_num = balance // a[i]
        balance -= purchase_num * a[i]
        balance += purchase_num * a[i+1]

print(balance)