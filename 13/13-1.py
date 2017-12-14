f1 = open('input.txt', 'r')

layers = {}
for i in f1.readlines():
	splitLine = i[:-1].split(': ')
	layers[int(splitLine[0])] = [int(splitLine[1]), 0, 1]
j = 0

caughtList = []
while j <= int(splitLine[0]):
	if j in layers:
		if layers[j][1] == 0:
			caughtList.append(j)
	for k in layers:
		layers[k][1] += layers[k][2]
		if layers[k][1] == layers[k][0] - 1 or layers[k][1] == 0:
			layers[k][2] *= -1
	j += 1
severity = 0
for l in caughtList:
	severity += l * layers[l][0]
print severity
