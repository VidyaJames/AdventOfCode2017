f1 = open('input.txt', 'r')

banks = [int(x) for x in f1.readline().split('\t')]
seenBefore = {}
steps = 1
seenBefore[tuple(banks)] = 0
answer = 0
while answer == 0:
	maxIndex = 0
	for i in range(len(banks)):
		if banks[i] > banks[maxIndex]:
			maxIndex = i
	traveseIndex = maxIndex
	j = banks[maxIndex]
	while j > 0:
		traveseIndex += 1
		if traveseIndex == len(banks):
			traveseIndex = 0
		banks[traveseIndex] += 1
		banks[maxIndex] -= 1
		j -= 1
	if tuple(banks) in seenBefore:
		answer = steps - seenBefore[tuple(banks)]
	else:
		seenBefore[tuple(banks)] = steps
		steps += 1
		
print answer
