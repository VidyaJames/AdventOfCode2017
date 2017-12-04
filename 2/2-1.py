f1 = open('input.txt', 'r')

differences = []
for i in f1.readlines():
	numbers = [int(x) for x in i.split('\t')]
	smallest = numbers[0]
	largest = numbers[0]
	for j in numbers:
		if (j > largest):
			largest = j
		elif (j < smallest):
			smallest = j
	differences.append(largest-smallest)
print sum(differences)
