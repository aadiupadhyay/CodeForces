n, s = int(input()), list(input())
ans = 0
for i in range(0, n, 2):
	if (s[i] == s[i + 1]):
		s[i] = chr(1 - ord(s[i]) + 2 * ord('a'))
		ans += 1
print(ans)
print(''.join(s))