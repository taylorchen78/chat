def read_file(fileName):
	content = []
	with open(fileName, 'r', encoding='utf-8-sig') as f:
		for line in f:
			content.append(line.strip())
		return content

def convert(textContent):
	output = []
	person = None
	for line in textContent:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
			output.append(person + ": " + line)
	return output

def write_file(fileName, lines):
	with open(fileName, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)


main()