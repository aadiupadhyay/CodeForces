t = int(input())
for iii in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	i = 0
	while i < n and a[i] >= i:
		i += 1
	flag = True
	while i < n:
		if a[i - 1] <= a[i]:
			a[i] = a[i - 1] - 1
		if a[i] < 0:
			print("No")
			flag = False
			break
		i += 1
	if flag:
		print("Yes")