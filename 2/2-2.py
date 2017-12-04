f1 = open('input.txt', 'r')

quotient = []
for i in f1.readlines():
	numbers = [int(x) for x in i.split('\t')]
	smallest = numbers[0]
	largest = numbers[0]
	for j in numbers:
		for k in numbers:
			if j % k == 0 and j != k:
				quotient.append(j/k)
print sum(quotient)
