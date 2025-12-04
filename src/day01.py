def main(input):
	lines = input.splitlines()
	res = 0
	res2 = 0
	currPos = 50
	
	for line in lines: 
		d = line[0]
		n = int(line[1:])
		for _ in range(n):
			if d == 'L':
				currPos = (currPos - 1) % 100
			else:
				currPos = (currPos + 1) % 100
			if currPos == 0:
				res2 += 1
		if currPos == 0:
			res += 1

	return [res, res2]