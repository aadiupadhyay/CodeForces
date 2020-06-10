for _ in range(int(input())):
	n=int(input())
	s=str(n)
	p=0
	while True:
		if len(s)==1:
			break
		p+=int(s[:-1]+'0')
		n=int(s[:-1])+int(s[-1])
		s=str(n)
	p=p+int(s)
	print(p)