f1 = open('input.txt', 'r')

instructions = [int(i) for i in f1.readlines()]
steps = 0
index = 0

while index < len(instructions) and index >= 0:
	move = instructions[index]
	if move >= 3:
		instructions[index] -= 1
	else:
		instructions[index] += 1
	index += move
	steps += 1
print steps
