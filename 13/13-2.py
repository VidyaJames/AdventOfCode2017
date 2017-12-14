f1 = open('input.txt', 'r')

layers = {}
for i in f1.readlines():
	splitLine = i[:-1].split(': ')
	layers[int(splitLine[0])] = {}
	layers[int(splitLine[0])]["depth"] = int(splitLine[1])
	layers[int(splitLine[0])]["pos"] = 0
	layers[int(splitLine[0])]["direction"] = 1

answer = -1
pico = 0
while answer == -1:
	pico += 1
	position = 0
	while position <= int(splitLine[0]):
		if position in layers:

			if (pico + position) % (2 * (layers[position]["depth"] - 1)) == 0:
				break
		position += 1
	if position > int(splitLine[0]):
		answer = pico	
print answer