def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())

	for line in lines:
		s = line.split(' ')
		time = s[0][:5]
		name = s[0][5:]
		print(name)


read_file('3.txt')