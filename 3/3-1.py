f1 = open('input.txt', 'r')

target = int(f1.readline())
boxLength = 1
while (boxLength**2 < target):
	boxLength += 2
	currentBase = boxLength**2

answer = 0 
if target == currentBase:
	answer = boxLength - 1
while answer == 0:
	i = 1
	while i <= (boxLength-1)/2:
		check = currentBase - i
		if target == check:
			answer = boxLength - 1 - i
		i += 1
	if answer == 0:
		currentBase -= (boxLength-1)/2
		i = 1
		while i <= (boxLength-1)/2:
			check = currentBase - i
			if target == check:
				answer = (boxLength-1)/2 + i
			i += 1
	currentBase -= (boxLength-1)/2
print answer
