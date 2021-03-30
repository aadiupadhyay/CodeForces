# aadiupadhyay mobile se code krte
for _ in range(int(input())):
	s = input()
	n = len(s)
	ind = -1
	ans = 1
	i = 1
	while i < n:
		if s[i] == s[i - 1] and s[i] == '1':
			ind = i
			break
		i += 1
	if ind != -1:
		j = n - 1
		while j >= ind:
			if s[j] == s[j - 1] and s[j] == '0':
				ans = 0
				break
			j -= 1

	print('YES' if ans else 'NO')
