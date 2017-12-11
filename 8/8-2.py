f1 = open('input.txt', 'r')

registers = {}
maxValue = 0
for line in f1.readlines():
	split = line[:-1].split(" ");
	if split[0] not in registers:
		registers[split[0]] = 0
	if split[4] not in registers:
		registers[split[4]] = 0
	doOp = 0
	compareString = str(registers[split[4]]) + split[5] + split[6]
	if eval(compareString):
		change = 1
		if split[1] == 'dec':
			change = -1
		registers[split[0]] += int(split[2]) * change
	if registers[split[0]] > maxValue:
		maxValue = registers[split[0]]
print maxValue
