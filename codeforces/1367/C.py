for i in range(int(input())):
	n, k = map(int, input().split())
	count = 0
	for i in ('0'*(k) + input() + '0'*(k)).split('1'):
		count += max((len(i) - k) // (k + 1), 0)
	print(count)