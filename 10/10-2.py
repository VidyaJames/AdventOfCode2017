f1 = open('input.txt', 'r')

sequence = list(xrange(256))
position = 0
skipSize = 0

inputs = list(f1.readline()[:-1])
asciiInputs = []
for g in inputs:
	asciiInputs.append(ord(str(g)))
asciiInputs.extend([17, 31, 73, 47, 23])

for h in range(0,64):
	for i in asciiInputs:
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
xors = []

for k in range (0,16):
	start = k * 16
	xor = 0
	for l in range (0,16):
		xor = xor ^ sequence[start+l]
	xors.append(xor)
hexStr = ""
for m in xors:
	hexNum = hex(m)[2:]
	if len(hexNum) == 1:
		hexNum = "0" + hexNum
	hexStr += hexNum
print hexStr
