f1 = open('input.txt', 'r')
input = f1.readline()
input = input[:-1]
i = 0
sum = 0
half=len(input)/2
while i < half:
	compare = i + half
	if (input[i] == input[compare]):
		sum += int(input[i])
	i += 1
print sum*2
