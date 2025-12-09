def main(input):
	res = 0
	res2 = 0
	#part 1
	for line in input.splitlines():
		bank = list(map(int, line.strip()))
		tens = max(bank[:-1])
		ones = max(bank[bank.index(tens)+1:])
		res += tens * 10 + ones

	#part 2
	for line in input.splitlines():
		bank = list(map(int, line.strip()))
		jolts = 0
		for index in range(11):
			digit = max(bank[:index -11])
			bank = bank[bank.index(digit) + 1:]
			jolts = (jolts * 10) + digit
		jolts = (jolts * 10) + max(bank)
		res2 += jolts
	return [res, res2]