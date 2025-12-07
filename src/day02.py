def main(input):
	res = 0
	res2 = 0
	ranges = input.split(",")
	
	for r in ranges:
		a,b = r.split("-")
		a = int(a)
		b = int(b)
		for i in range(a,b+1):
			l = len(str(i))
			x = str(i)[:l//2]
			y = str(i)[l//2:]
			if x == y:
				res += i

			s = str(i)
			for j in range(2, len(s) +1):
				if len(s) % j == 0 and s[:len(s) // j] * j == s:
					res2 += i
					break

	return [res, res2]