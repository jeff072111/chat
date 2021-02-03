def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
		return lines

#名單切割，計算字數
def convert(lines):
	person = None
	台南家電_word_count = 0
	台南家電_sticker_count = 0
	台南家電_image_count = 0
	祈翰Jeffrey_word_count = 0
	祈翰Jeffrey_sticker_count = 0
	祈翰Jeffrey_image_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == '台南佳電':
			if s[2] == '貼圖':
				台南家電_sticker_count += 1
			elif  s[2] == '圖片':
				台南家電_image_count += 1
			else:
				for m in s[2:]:
					台南家電_word_count += len(m)
			
		elif name == '祈翰Jeffrey':
			if s[2] == '貼圖':
				祈翰Jeffrey_sticker_count += 1
			elif  s[2] == '圖片':
				祈翰Jeffrey_image_count += 1
			else:
				for m in s[2:]:
					祈翰Jeffrey_word_count += len(m)

	print('台南佳電','說了:', 台南家電_word_count, '個字')
	print('台南佳電','傳了:', 台南家電_sticker_count, '個貼圖')
	print('台南佳電','傳了:', 台南家電_image_count, '個圖片')
	print('祈翰Jeffrey','說了:', 祈翰Jeffrey_word_count, '個字')
	print('祈翰Jeffrey','傳了:', 祈翰Jeffrey_sticker_count, '個貼圖')
	print('祈翰Jeffrey','傳了:', 祈翰Jeffrey_image_count, '個圖片')


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('[LINE]台南佳電.txt')
	lines = convert(lines)
	# write_file('output.txt', lines)


main()