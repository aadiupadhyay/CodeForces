q = int(input())
data = []
for _ in range(q):
	data.append(input().split())
l = 0
r = 1
b = {}
for i in data:
	id_ = i[1]
	id = int(i[1])
	if i[0] == 'L':
		b[id_] = l
		l -= 1
	if i[0] == 'R':
		b[id_] = r
		r += 1
	if i[0] == '?':
		p = b[id_]
		print(min(p-l-1, r-p-1))