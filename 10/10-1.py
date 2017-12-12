f1 = open('input.txt', 'r')

sequence = list(xrange(256))
position = 0
skipSize = 0

inputs = f1.readline()[:-1].split(",")

for i in inputs:
	i = int(i)
	reverseList = []
	j = 0
	while j < i:
		index = position + j
		reverseList.append(sequence[index % len(sequence)])
		j += 1
	reverseList = list(reversed(reverseList))
	j = 0
	while j < i:
		index = position+j
		sequence[index % len(sequence)] = reverseList[j]
		j += 1
	position = (i + position + skipSize) % len(sequence)
	skipSize += 1	
print sequence[0] * sequence[1]
